# camera.py

from datetime import datetime
import subprocess
import time
import os
from pathlib import Path

# Set directory for raw photos
RAW_DIR = Path("./static/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def takePhoto(filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"raw_{timestamp}.jpg"
    
    filepath = RAW_DIR / filename

    subprocess.run([
        "gphoto2",
        "--capture-image-and-download",
        f"--filename={filepath}"
    ])

    return filepath


def takeMultiplePhoto(count=4, delay=2):
    photo_paths = []
    for i in range(count):
        photo_path = takePhoto()
        photo_paths.append(photo_path)
        if i  < count -1:
            time.sleep(delay)
    
    return photo_paths

def clearRawPhotos():
    for file in RAW_DIR.glob("*.jpg"):
        try:
            file.unlink()
        except Exception as error:
            print(f"Error deleting {file}: {e}")