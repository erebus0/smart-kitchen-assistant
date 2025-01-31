# test_all_components.py
from picamera2 import Picamera2
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time
import os

def test_all():
    # Initialize components
    reader = SimpleMFRC522()
    picam2 = None
    
    try:
        # Test camera
        print("Testing camera...")
        picam2 = Picamera2()
        config = picam2.create_still_configuration()
        picam2.configure(config)
        picam2.start()
        print("Camera initialized ✓")
        
        # Test RFID
        print("\nTesting RFID reader...")
        print("Please place a tag on the reader")
        id, text = reader.read()
        print(f"RFID read successful ✓")
        print(f"ID: {id}")
        print(f"Text: {text}")
        
        # Take a photo
        print("\nTaking a test photo...")
        picam2.capture_file("component_test.jpg")
        print("Photo saved as 'component_test.jpg' ✓")
        
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        if picam2:
            picam2.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    test_all()
