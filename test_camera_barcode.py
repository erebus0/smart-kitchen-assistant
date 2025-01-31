from src.camera.camera_manager import CameraManager
from src.barcode.barcode_scanner import BarcodeScanner
import time

def test_camera_and_barcode():
    print("Initializing camera...")
    camera = CameraManager()
    
    try:
        print("Starting camera...")
        camera.start()
        
        print("Creating barcode scanner...")
        scanner = BarcodeScanner(camera)
        
        print("\nReady to scan! Press Ctrl+C to exit")
        print("Hold a barcode in front of the camera...")
        
        while True:
            result = scanner.scan_barcode(save_debug_image=True)
            
            if result:
                print(f"\nBarcode detected!")
                print(f"Type: {result['type']}")
                print(f"Data: {result['data']}")
                
            time.sleep(1)  # Wait a second between scans
            
    except KeyboardInterrupt:
        print("\nStopping test...")
    
    finally:
        print("Cleaning up...")
        camera.stop()

if __name__ == "__main__":
    test_camera_and_barcode()
