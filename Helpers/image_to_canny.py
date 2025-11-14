import os
import cv2
from pathlib import Path

# Input and output paths
input_folder = Path("/kaggle/input/canny-tuples/dataset/images")
output_folder = Path("/kaggle/input/canny-tuples/dataset/canny")

# Create output folder if not exists
output_folder.mkdir(parents=True, exist_ok=True)

# Allowed image formats
valid_ext = {".jpg", ".jpeg", ".png"}

print(f"Converting images from: {input_folder}")
print(f"Saving canny images to: {output_folder}")

for img_path in input_folder.iterdir():
    if img_path.suffix.lower() not in valid_ext:
        continue
    
    # Read image
    img = cv2.imread(str(img_path))
    if img is None:
        print(f"Skipping unreadable file: {img_path}")
        continue
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)
    
    # Save output as 3-channel (optional)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Save with same filename
    save_path = output_folder / img_path.name
    cv2.imwrite(str(save_path), edges_rgb)

print("✅ Canny conversion completed!")
print(f"Total saved: {len(list(output_folder.iterdir()))}")
