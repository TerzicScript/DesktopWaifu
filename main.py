import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMenu, QAction, QActionGroup, QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

class AnimeMascot(QWidget):
    def __init__(self, gif_path):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.native_size = None

        self.label = QLabel(self)
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)

        self.scale_factor = 1.0
        self.current_opacity = 1.0
        self.current_speed = 100

        self.op_group = QActionGroup(self)
        self.sc_group = QActionGroup(self)
        self.sp_group = QActionGroup(self)

        self.movie.frameChanged.connect(self.init_size)
        self.movie.start()

        self.show()
        self.drag_pos = None

    def update_dimensions(self):
        if not self.native_size:
            return

        self.movie.blockSignals(True)
        self.movie.stop()

        new_size = self.native_size * self.scale_factor

        self.movie.setScaledSize(new_size)

        self.label.setMovie(None)
        self.label.setMovie(self.movie)
        self.label.setFixedSize(new_size)
        self.setFixedSize(new_size)

        self.movie.start()
        self.movie.blockSignals(False)

    def init_size(self):
        try:
            self.movie.frameChanged.disconnect(self.init_size)
        except (TypeError, RuntimeError):
            pass

        rect = self.movie.frameRect()
        if rect.isValid():
            self.native_size = rect.size()

        self.update_dimensions()

    def load_new_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select GIF", "", "GIF Files (*.gif)")
        if file_path:
            self.native_size = None
            self.movie.stop()
            self.movie.setFileName(file_path)
            self.movie.setSpeed(self.current_speed)
            self.movie.frameChanged.connect(self.init_size)
            self.movie.start()

    def contextMenuEvent(self, event):
        for group in [self.op_group, self.sc_group, self.sp_group]:
            for action in group.actions():
                group.removeAction(action)

        menu = QMenu(self)

        change_act = menu.addAction("Change Model")
        change_act.triggered.connect(self.load_new_model)
        menu.addSeparator()

        opacity_menu = menu.addMenu("Opacity")
        self.op_group.setExclusive(True)
        for val in [1.0, 0.8, 0.6, 0.4]:
            act = QAction(f"{int(val * 100)}%", self, checkable=True)
            act.setActionGroup(self.op_group)
            act.setChecked(val == self.current_opacity)
            act.triggered.connect(lambda chk, v=val: self.change_opacity(v))
            opacity_menu.addAction(act)

        scale_menu = menu.addMenu("Scale")
        self.sc_group.setExclusive(True)
        for s in [0.5, 1.0, 1.5, 2.0]:
            act = QAction(f"x{s}", self, checkable=True)
            act.setActionGroup(self.sc_group)
            act.setChecked(s == self.scale_factor)
            act.triggered.connect(lambda chk, v=s: self.change_scale(v))
            scale_menu.addAction(act)

        speed_menu = menu.addMenu("Speed")
        self.sp_group.setExclusive(True)
        for label, v in {"Slow": 50, "Normal": 100, "Fast": 150}.items():
            act = QAction(label, self, checkable=True)
            act.setActionGroup(self.sp_group)
            act.setChecked(v == self.current_speed)
            act.triggered.connect(lambda chk, v=v: self.change_speed(v))
            speed_menu.addAction(act)

        menu.addSeparator()
        exit_act = menu.addAction("❌ Exit")
        exit_act.triggered.connect(QApplication.instance().quit)

        menu.exec_(self.mapToGlobal(event.pos()))

    def change_opacity(self, val):
        self.current_opacity = val
        self.setWindowOpacity(val)

    def change_speed(self, val):
        self.current_speed = val
        self.movie.setSpeed(val)

    def change_scale(self, factor):
        self.scale_factor = factor
        self.update_dimensions()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos is not None:
            self.move(event.globalPos() - self.drag_pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mascot = AnimeMascot("gifs/Evernight.gif")
    sys.exit(app.exec_())