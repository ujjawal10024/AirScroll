# 🖐 AirScroll 

AirScroll is a real-time gesture-controlled scrolling and screenshot tool built using OpenCV and MediaPipe.

It allows users to control vertical scrolling and capture screenshots using simple hand gestures detected via webcam.

---

## 🚀 Features

- 👍 Thumbs Up → Toggle scrolling ON/OFF
- ✋ Open Palm → Capture screenshot
- 🤏 Pinch Gesture → Set neutral scroll position
- Smooth scrolling algorithm
- Deadzone filtering to prevent jitter
- Multi-monitor screenshot detection
- Modular Python package structure

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- PyAutoGUI
- MSS

---

## 🧠 How It Works

1. MediaPipe detects 21 hand landmarks in real time.
2. Custom gesture logic compares landmark positions.
3. Based on gesture:
   - Scroll is toggled
   - Screenshot is captured
   - Neutral position is calibrated.
4. Scroll speed is smoothed using exponential smoothing.
5. Screenshots are saved with timestamp-based filenames.

---

## 📁 Project Structure

airscroll/
│
├── airscroll/
│   ├── __init__.py
│   ├── config.py
│   ├── gestures.py
│   ├── screenshot.py
│   └── main.py
│
├── screenshots/
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/airscroll.git  
cd airscroll

Create virtual environment (recommended):

python -m venv venv  
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python -m airscroll.main

---

## 🎯 Configuration

All tunable parameters are located inside:

airscroll/config.py

You can adjust:
- Detection confidence
- Gesture cooldown timers
- Scroll sensitivity
- Smoothing factor
- Pinch threshold

---

## 📸 Screenshots

Screenshots are automatically saved inside the `screenshots/` folder.

---

## 🔮 Future Improvements

- Horizontal scrolling support
- Gesture calibration mode
- GUI settings panel
- Custom gesture classifier using ML
- Window-specific screenshot capture

---

## 📌 Resume Description

Built a real-time gesture-controlled scrolling and screenshot system using OpenCV and MediaPipe with modular architecture and smooth scroll optimization.

---

## 👨‍💻 Author

Ujjawal Shakya
ujjawalshakya94@gmail.com
