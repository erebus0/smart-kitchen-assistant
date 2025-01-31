# test_all.py
import time
from picamera2 import Picamera2
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

def test_camera():
    try:
        print("\nTesting Camera...")
        picam2 = Picamera2()
        picam2.start()
        time.sleep(2)
        picam2.capture_file("test.jpg")
        print("Camera test successful - saved test.jpg")
        picam2.stop()
    except Exception as e:
        print(f"Camera Error: {e}")

def test_rfid():
    try:
        print("\nTesting RFID...")
        reader = SimpleMFRC522()
        print("Place an RFID tag near the reader...")
        id, text = reader.read()
        print(f"Tag detected! ID: {id}")
        print(f"Text: {text}")
    except Exception as e:
        print(f"RFID Error: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    print("Starting hardware tests...")
    test_camera()
    test_rfid()
