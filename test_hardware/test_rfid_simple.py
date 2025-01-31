# test_hardware/test_rfid_simple.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rfid.rfid_handler import RFIDHandler
import time

def test_gpio_spi():
    print("Testing GPIO and SPI setup...")
    
    try:
        rfid = RFIDHandler()
        print("RFID Handler created successfully")
        
        print("\nAttempting to read...")
        result = rfid.read_tag()
        if result:
            print(f"Communication test successful: {result}")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        print("\nTest complete")

if __name__ == "__main__":
    test_gpio_spi()
