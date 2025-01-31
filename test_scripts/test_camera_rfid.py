# test_scripts/test_camera_rfid.py

import sys
import time
sys.path.append('..')  # Add parent directory to path

from src.camera.camera_manager import CameraManager
from src.rfid.rfid_manager import RFIDManager

def test_system():
    print("=== Testing Camera and RFID Systems ===")
    
    # Initialize components
    camera = CameraManager()
    rfid = RFIDManager()
    
    try:
        print("\nStarting camera...")
        camera.start()
        
        print("\nSystem ready! Waiting for RFID tags...")
        print("Place an RFID tag near the reader (Ctrl+C to exit)")
        
        while True:
            result = rfid.read_tag()
            if result:
                print(f"\nRFID Tag detected!")
                print(f"ID: {result['tag_id']}")
                print(f"Text: {result['text']}")
                
                # Capture image when tag is detected
                image_path = camera.capture_image(result['tag_id'])
                if image_path:
                    print(f"Image saved to: {image_path}")
                
                print("\nWaiting for next tag...")
            
            time.sleep(0.1)  # Short sleep to prevent CPU overload
            
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    finally:
        camera.stop()
        rfid.cleanup()
        print("Cleanup complete")

if __name__ == "__main__":
    test_system()
