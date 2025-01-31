# test_camera_handler.py

from src.camera.camera_handler import CameraHandler
import time

def test_camera():
    camera = CameraHandler()
    
    print("Testing basic photo capture...")
    photo_path = camera.take_photo()
    if photo_path:
        print(f"Basic photo captured: {photo_path}")
    
    time.sleep(2)
    
    print("\nTesting barcode-optimized capture...")
    barcode_path = camera.capture_for_barcode()
    if barcode_path:
        print(f"Barcode photo captured: {barcode_path}")

if __name__ == "__main__":
    test_camera()
