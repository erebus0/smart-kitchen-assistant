# test_hardware/test_camera_handler.py
import sys
import os
import time

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.camera.camera_handler import CameraHandler

def test_camera():
    try:
        camera = CameraHandler()
        
        print("Testing basic photo capture...")
        photo_path = camera.take_photo()
        if photo_path:
            print(f"Basic photo captured: {photo_path}")
        else:
            print("Basic photo capture failed")
        
        time.sleep(1)  # Reduced wait time
        
        print("\nTesting barcode-optimized capture...")
        barcode_path = camera.capture_for_barcode()
        if barcode_path:
            print(f"Barcode photo captured: {barcode_path}")
        else:
            print("Barcode photo capture failed")
            
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"Test error: {e}")

if __name__ == "__main__":
    test_camera()
