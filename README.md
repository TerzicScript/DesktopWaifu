# 🌸 Desktop Waifu v1.0.0

<div align="center">

**A lightweight, GIF desktop companion tool that brings your favorite animated characters to life on your screen.**

[Download Latest Release](https://github.com/TerzicScript/DesktopWaifu/releases) • [Report Bug](https://github.com/TerzicScript/DesktopWaifu/issues) • [Request Feature](https://github.com/TerzicScript/DesktopWaifu/issues)

</div>

## 🎯 Overview

**Desktop Waifu** is a lightweight Python application built with PyQt5 that allows you to have animated companions on your desktop. These companions stay "always on top" of your other windows, providing a customizable digital presence while you work or play.

---

## ⚙️ How It Works

The application is designed to be portable and simple. It looks for a specific folder structure to load your animations.

1.  **Placement**: Place the executable (`DesktopWaifu.exe`) and a folder named `gifs` in the same directory. ( Extract DesktopWaifu_v1.0.0.zip )
2.  **Required File**: Inside the `gifs` folder, there must be a file named `Evernight.gif`.
3.  **Execution**: When you run the program, it automatically pulls `Evernight.gif` and starts the playback on your desktop.

**Directory Structure:**
```text
Project_Folder/
├── DesktopWaifu.exe (or main.py)
└── gifs/
    └── Evernight.gif
```

---

### Why This Tool?

- No clue, it's free?

---

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| Always on Top | Companion stays visible above all other active windows |
| Lightweight | Minimal CPU and RAM usage, perfect for low-end systems |
| Dynamic Scaling | Resize your GIF instantly to fit your screen layout |
| Opacity Control | Adjust transparency for a subtle or solid look |
| Speed Control | Fine-tune the playback speed of the animation |
| GIF Swapping | Change your companion on the fly through the context menu |

---

## 💾 Download & Installation

### Option 1: Run from Source

**Requirements:**
- Python 3.10 or higher
- pip package manager

**Installation Steps:**

```bash
# Clone the repository
git clone https://github.com/TerzicScript/DesktopWaifu.git
cd DesktopWaifu

# Install dependencies
pip install PyQt5

# Run the application
python main.py
```

### Option 2: Pre-Built Executable

1. Go to the [Releases Page](https://github.com/yourusername/desktop-waifu/releases)
2. Download ```DesktopWaifu.exe```
3. Download gifs folder and put it in same directory as .exe file ( only Evernight.gif is needed )
4. Run and enjoy - no installation needed!

---

## 🛠 Building the Executable

If you want to compile the Python script into a standalone Windows executable with the custom icon, follow these steps:

**Requirements:**
- PyInstaller: ```pip install pyinstaller```
- Icon file: ```mainIco.ico``` in the root directory. ( THIS IS REALLY REALLY IMPORTANT )

**Build Command:**
Run this in your terminal to create a single-file executable named **DesktopWaifu**:

```bash
pyinstaller --noconsole --onefile --icon=mainIco.ico --name="DesktopWaifu" main.py
```

* ```--noconsole```: Hides the black terminal window when the app runs.
* ```--onefile```: Bundles everything into a single .exe.
* ```--icon```: Sets the custom ```mainIco.ico``` as the application icon.

---

## 🚀 Quick Start Guide

### Step 1: Launch
Run ```python main.py``` or open the ```.exe```. A default character will appear on your screen.

### Step 2: Position
Left-click and drag the character to place them anywhere on your desktop.

### Step 3: Customize
Right-click on the character to open the **Settings Menu**:
- **Load GIF**: Choose any ```.gif``` file from your computer.
- **Scale**: Change the size of the character.
- **Opacity**: Adjust transparency (0% - 100%).
- **Speed**: Speed up or slow down the animation.

---

## 💻 System Requirements

- **OS**: Windows 10/11, macOS, or Linux
- **RAM**: 2GB Minimum
- **Graphics**: Any integrated or dedicated GPU
- **Python**: 3.8+ (if running from source)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (```git checkout -b feature/AmazingFeature```)
3. Commit your changes (```git commit -m 'Add AmazingFeature```')
4. Push to the branch (```git push origin feature/AmazingFeature```)
5. Open a Pull Request

## 🙏 Credits

- **PyQt5 Team** - For the robust UI framework.
- **My Lonely Ass** - For creating this stupid project in first place...

---

<div align="center">

[⬆ Back to Top](#-desktop-waifu-v100)

</div>
