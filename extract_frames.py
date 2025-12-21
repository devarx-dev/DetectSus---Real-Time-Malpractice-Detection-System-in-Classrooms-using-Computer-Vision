import cv2
import os

# Create frames_raw folder if not exists
os.makedirs("frames_raw", exist_ok=True)

# Path to your video file (.mov)
video_path = "videos/malpractice.mov"

# Load the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Cannot open video. Check path & filename.")
    exit()

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    filename = f"frames_raw/frame_{count}.jpg"
    cv2.imwrite(filename, frame)
    count += 1

cap.release()
print(f"✅ Frames extracted: {count}")
