**Reel-Shorts Controller**

This Python project lets you control YouTube Shorts or Instagram Reels using simple hand gestures detected via your webcam. Instead of using keyboard keys or mouse clicks, you navigate videos by moving your **thumb down to go to the next reel** and your **index finger down to go to the previous reel**.

The project uses **MediaPipe** for real-time hand landmark detection, **OpenCV** for video capture, and **pyautogui** to simulate keyboard presses for scrolling.

This version **removes the mouth control gesture** to make the interaction easier and less tiring for your face and to focus purely on hand gestures.

Ideal for beginners on Windows 10, especially those with slower laptops, with an easy setup guide and virtual environment instructions.

---


# Reel-Shorts Controller (Hand Gesture Control for YouTube Shorts)

Control your YouTube Shorts or Instagram Reels with simple hand gestures — no mouse or keyboard needed!

---

## Features

- **Thumb down movement:** Move to the next reel  
- **Index finger down movement:** Move to the previous reel  
- Uses your webcam to detect hand movements in real-time  
- Lightweight and beginner-friendly  
- No more mouth control — so your face won’t get tired!

---

## Setup Instructions (Windows 10)

### 1. Download or clone this repository

```bash
git clone https://github.com/yourusername/reel-shorts-controller.git
cd reel-shorts-controller
````

Or just download the `.py` file directly.

---

### 2. Create and activate a virtual environment (recommended)

Open **PowerShell** or **Command Prompt**:

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment:
# In PowerShell:
.\venv\Scripts\Activate.ps1

# Or in Command Prompt:
.\venv\Scripts\activate.bat
```

---

### 3. Install dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

---

### 4. Run the script

```bash
python your_script_name.py
```

---

### 5. How to use

* Make sure your webcam is working and accessible
* Show your **thumb moving downward** to move to the **next reel**
* Show your **index finger moving downward** to move to the **previous reel**
* Press `q` anytime to quit the program

---

## Tips and Troubleshooting

* Close other programs that might use the webcam
* Run the script as Administrator if keyboard controls don’t work
* On slower laptops, close unused apps to improve performance
* Keep your hand gestures clear and within the webcam’s view for best results

---

## License

MIT License (feel free to modify and share)

---

Made with ❤️ and hand gestures by AD
