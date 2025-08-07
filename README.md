
A simple Python project that performs **real-time face detection** on a video file using OpenCV’s Haar Cascade classifier.

---

##  How It Works

1. Loads OpenCV's pre-trained Haar Cascade face detector.
2. Opens and processes the video file frame by frame.
3. Converts each frame to grayscale for efficient detection.
4. Detects faces and draws green rectangles around them.
5. Displays the result in a real-time window.

---

### Requirements

- Python 3.6 or higher
- OpenCV library

### Install Dependencies

pip install opencv-python


Run the Script
 1. Place your video file in the same folder.
 2. Rename it to test_video.mp4
 3. In your terminal or command prompt, run:

python face_detection.py


⸻

Tips
 • If no faces are detected:
 • Try increasing scaleFactor to 1.2
 • Or reduce minNeighbors to 3
 • Make sure the video has clear lighting and visible faces

⸻

Notes
 • The video file test_video.mp4 is not included in the repository due to size limits.
You can add your own test video manually.

⸻

Technologies Used
 • Python
 • OpenCV
 • Haar Cascade Classifier
