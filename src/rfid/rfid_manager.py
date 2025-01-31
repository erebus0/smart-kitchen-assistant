# src/rfid/rfid_manager.py

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from datetime import datetime

class RFIDManager:
    def __init__(self):
        self.reader = SimpleMFRC522()
        self.last_read = None
        self.last_read_time = None
        
    def read_tag(self):
        """
        Read an RFID tag
        Returns: Dictionary with tag_id and text if successful, None otherwise
        """
        try:
            id, text = self.reader.read()
            current_time = datetime.now()
            
            # Prevent duplicate reads within 2 seconds
            if (self.last_read == id and 
                self.last_read_time and 
                (current_time - self.last_read_time).total_seconds() < 2):
                return None
            
            self.last_read = id
            self.last_read_time = current_time
            
            return {
                'tag_id': str(id),
                'text': text.strip(),
                'timestamp': current_time.isoformat()
            }
            
        except Exception as e:
            print(f"Error reading RFID: {e}")
            return None
    
    def write_tag(self, text):
        """Write data to an RFID tag"""
        try:
            self.reader.write(text)
            return True
        except Exception as e:
            print(f"Error writing to RFID: {e}")
            return False
    
    def cleanup(self):
        """Clean up GPIO resources"""
        GPIO.cleanup()
