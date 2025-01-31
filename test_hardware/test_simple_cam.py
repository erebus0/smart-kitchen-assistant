# test_simple_cam.py
from picamera2 import Picamera2
import time

def main():
    try:
        # Initialize camera
        picam = Picamera2()
        print("Camera initialized")
        
        # Configure camera
        config = picam.create_still_configuration()
        picam.configure(config)
        print("Camera configured")
        
        # Start camera
        picam.start()
        print("Camera started")
        
        # Wait for auto-exposure
        time.sleep(2)
        
        # Take a picture
        picam.capture_file("test.jpg")
        print("Picture captured: test.jpg")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            picam.stop()
            print("Camera stopped")
        except:
            pass

if __name__ == "__main__":
    main()
