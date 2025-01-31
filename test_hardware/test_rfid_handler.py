# test_hardware/test_rfid_handler.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rfid.rfid_handler import RFIDHandler
import time

def test_rfid():
    rfid = RFIDHandler()
    
    try:
        # Test writing to tag
        print("Testing RFID write...")
        print("Place a tag to write to...")
        success = rfid.write_tag("Test item " + time.strftime("%Y%m%d-%H%M%S"))
        if success:
            print("Write successful!")
        else:
            print("Write failed!")
            
        time.sleep(2)
        
        # Test reading from tag
        print("\nTesting RFID read...")
        print("Place a tag to read...")
        result = rfid.read_tag()
        
        if result:
            print("\nTag detected!")
            print(f"ID: {result['tag_id']}")
            print(f"Text: {result['text']}")
            print(f"Time: {result['timestamp']}")
        else:
            print("No tag read")
            
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"Test error: {e}")

if __name__ == "__main__":
    test_rfid()
