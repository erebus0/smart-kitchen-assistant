# test_rfid.py
import RPi.GPIO as GPIO
import time

RESET_PIN = 22    # Pin 22
MISO_PIN = 9      # Pin 21
MOSI_PIN = 10     # Pin 19
SCK_PIN = 11      # Pin 23
CS_PIN = 8        # Pin 24

def test_rfid():
    try:
        print("Setting up GPIO...")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RESET_PIN, GPIO.OUT)
        GPIO.setup(CS_PIN, GPIO.OUT)
        GPIO.setup(MOSI_PIN, GPIO.OUT)
        GPIO.setup(MISO_PIN, GPIO.IN)
        GPIO.setup(SCK_PIN, GPIO.OUT)
        
        print("GPIO setup complete")
        print("Please check physical connections:")
        print(f"RESET -> GPIO{RESET_PIN}")
        print(f"MISO  -> GPIO{MISO_PIN}")
        print(f"MOSI  -> GPIO{MOSI_PIN}")
        print(f"SCK   -> GPIO{SCK_PIN}")
        print(f"CS    -> GPIO{CS_PIN}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    test_rfid()
