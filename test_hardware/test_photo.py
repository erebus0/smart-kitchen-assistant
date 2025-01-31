# test_photo.py
from picamera2 import Picamera2
import time

def take_photo():
    print("Initializing camera...")
    picam2 = Picamera2()
    
    print("Creating camera configuration...")
    config = picam2.create_still_configuration()
    picam2.configure(config)
    
    print("Starting camera...")
    picam2.start()
    time.sleep(2)  # Warm up time
    
    print("Taking photo...")
    picam2.capture_file("python_test.jpg")
    print("Photo saved as python_test.jpg")
    
    picam2.close()
    print("Camera closed")

if __name__ == "__main__":
    take_photo()
