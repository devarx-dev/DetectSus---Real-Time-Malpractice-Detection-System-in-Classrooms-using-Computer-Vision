import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
frames_folder = "frames_raw"  # where your extracted frames are stored
dataset_folder = "dataset"

# New structure
img_train = "dataset/images/train"
img_val = "dataset/images/val"
lbl_train = "dataset/labels/train"
lbl_val = "dataset/labels/val"

# Create folders
folders = [img_train, img_val, lbl_train, lbl_val]
for f in folders:
    os.makedirs(f, exist_ok=True)

# Get all frame file names
all_images = [f for f in os.listdir(frames_folder) if f.endswith(".jpg")]

# Train-val split (80/20)
train_imgs, val_imgs = train_test_split(all_images, test_size=0.2, random_state=42)

# Move images (labels will be added later)
def move_images(img_list, target_folder):
    for img in img_list:
        src = os.path.join(frames_folder, img)
        dst = os.path.join(target_folder, img)
        shutil.copy(src, dst)

# Copy images
move_images(train_imgs, img_train)
move_images(val_imgs, img_val)

print("✅ Dataset structure created successfully!")
print(f"Train images: {len(train_imgs)}")
print(f"Val images: {len(val_imgs)}")
