# src/rfid/rfid_handler.py
import RPi.GPIO as GPIO
import spidev
import time
from datetime import datetime

class RFIDHandler:
    # MFRC522 Registers
    RST_PIN = 25  # Pin 22
    CS_PIN = 8    # Pin 24
    MISO_PIN = 9  # Pin 21
    MOSI_PIN = 10 # Pin 19
    SCK_PIN = 11  # Pin 23

    def __init__(self):
        try:
            # Initialize GPIO
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            
            # Setup GPIO pins
            GPIO.setup(self.RST_PIN, GPIO.OUT)
            GPIO.setup(self.CS_PIN, GPIO.OUT)
            
            # Initialize SPI
            self.spi = spidev.SpiDev()
            self.spi.open(0, 0)  # Bus 0, Device 0
            self.spi.max_speed_hz = 1000000  # 1MHz
            
            # Reset the RFID reader
            GPIO.output(self.RST_PIN, GPIO.HIGH)
            time.sleep(0.1)
            
            print("RFID Handler initialized successfully")
            
        except Exception as e:
            print(f"Error initializing RFID Handler: {e}")
            self.cleanup()
            raise

    def read_tag(self):
        """Attempt to read an RFID tag"""
        try:
            # Simple test read
            self.spi.xfer2([0x00])  # Null command to test communication
            print("SPI communication successful")
            return {"tag_id": "test", "timestamp": datetime.now().isoformat()}
        except Exception as e:
            print(f"Error reading tag: {e}")
            return None
        
    def cleanup(self):
        """Cleanup resources"""
        try:
            self.spi.close()
            GPIO.cleanup()
        except:
            pass

    def __del__(self):
        self.cleanup()
