import cv2
import os

# Folder to save selected frames
os.makedirs("frames_raw", exist_ok=True)

# Video path
video_path = "videos/malpractice.mov"

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Cannot open video. Check path & filename.")
    exit()

# Total frames in video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Total frames in video: {total_frames}")

# Number of frames you want
num_frames_to_extract = 50

# Interval between frames
interval = total_frames // num_frames_to_extract

count = 0
saved = 0

while saved < num_frames_to_extract:
    cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    ret, frame = cap.read()

    if not ret:
        break

    filename = f"frames_raw/frame_{saved}.jpg"
    cv2.imwrite(filename, frame)

    saved += 1
    count += interval

cap.release()
print(f"✅ Successfully extracted {saved} frames")
