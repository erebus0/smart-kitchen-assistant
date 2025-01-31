# src/camera/camera_handler.py
import subprocess
import os
from datetime import datetime

class CameraHandler:
    def __init__(self, image_dir="data/images"):
        self.image_dir = image_dir
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

    def take_photo(self, filename=None):
        """Take a photo using libcamera-jpeg with shorter timeout"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.jpg"
        
        full_path = os.path.join(self.image_dir, filename)
        
        try:
            # Reduced timeout to 1 second
            result = subprocess.run([
                'libcamera-jpeg',
                '-o', full_path,
                '-t', '1000',  # 1 second timeout
                '--width', '1296',
                '--height', '972',
                '--nopreview'  # Disable preview window
            ], check=True, timeout=2)  # 2 second process timeout
            
            if os.path.exists(full_path):
                print(f"Photo saved: {full_path}")
                return full_path
            else:
                print("Error: Photo file not created")
                return None
                
        except subprocess.TimeoutExpired:
            print("Error: Camera capture timed out")
            return None
        except subprocess.CalledProcessError as e:
            print(f"Error taking photo: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def capture_for_barcode(self):
        """Take a photo optimized for barcode scanning"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"barcode_{timestamp}.jpg"
        full_path = os.path.join(self.image_dir, filename)
        
        try:
            result = subprocess.run([
                'libcamera-jpeg',
                '-o', full_path,
                '-t', '1000',
                '--width', '2592',
                '--height', '1944',
                '--shutter', '20000',
                '--nopreview'
            ], check=True, timeout=2)
            
            if os.path.exists(full_path):
                print(f"Barcode photo saved: {full_path}")
                return full_path
            return None
            
        except Exception as e:
            print(f"Error capturing barcode image: {e}")
            return None
