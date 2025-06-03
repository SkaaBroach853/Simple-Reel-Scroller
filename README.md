# Reel-Shorts Controller (Thumb & Index Edition)

Control YouTube Shorts or Instagram Reels using just two fingers!

🎯 **Thumb down = Next reel**  
🎯 **Index finger down = Previous reel**

This version is lightweight, easy to set up, and designed for smooth use even on slower Windows 10 laptops. No face gestures, no fuss — just your hand and webcam!

---

## 🛠️ Setup Instructions

### 1. Clone or Download

```bash
git clone https://github.com/yourusername/reel-shorts-controller.git
cd reel-shorts-controller
````

Or simply download the `.py` file.

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate on PowerShell
.\venv\Scripts\Activate.ps1

# Or on Command Prompt
.\venv\Scripts\activate.bat
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Run the Controller

```bash
python reel_controller.py
```

---

## 🧠 How It Works

* **Thumb Tip (landmark 4)** moves down → `pyautogui.press('down')`
* **Index Finger Tip (landmark 8)** moves down → `pyautogui.press('up')`
* Real-time detection using your webcam via MediaPipe

---

## 🎮 Usage

* Start the program
* Keep your hand within webcam view
* Move your **thumb** downward → Go to **next reel**
* Move your **index finger** downward → Go to **previous reel**
* Press `q` to quit anytime

---

## 💡 Tips

* Good lighting helps detect hands better
* Close background apps to improve performance
* Keep one hand visible, steady, and gesture clearly

---

## 🤹 Fun Upload Tip

Want to upload your awesome finger-powered code to GitHub?

```bash
git add .
git commit -m "Two fingers, zero problems. Removed mouth, now just pointing at greatness."
git push
```

🚀 Congratulations, you're a finger-scrolling wizard.

---

## 📜 License

MIT – Free to modify and share

---

Made with ❤ and 😄 by AD
