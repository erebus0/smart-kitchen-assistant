from .database.db_manager import KitchenDatabase
from .camera.camera_manager import CameraManager
from .barcode.barcode_scanner import BarcodeScanner
from .rfid.rfid_manager import RFIDManager
import time
from datetime import datetime

class KitchenController:
    def __init__(self):
        """Initialize all components of the kitchen assistant"""
        # Initialize database
        self.database = KitchenDatabase()
        
        # Initialize camera and barcode scanner
        self.camera = CameraManager()
        self.barcode_scanner = BarcodeScanner(self.camera)
        
        # Initialize RFID manager
        self.rfid_manager = RFIDManager()
        
        # Track system state
        self.is_running = False
    
    def start(self):
        """Start all systems"""
        print("Starting Kitchen Assistant...")
        self.is_running = True
        self.camera.start()
        
    def stop(self):
        """Safely shut down all systems"""
        print("Shutting down Kitchen Assistant...")
        self.is_running = False
        self.camera.stop()
        self.database.close()
    
    def add_item(self, identification, name, expiry_date=None):
        """
        Add an item to the system
        identification can be either barcode or RFID tag
        """
        try:
            self.database.add_item(identification, name, expiry_date)
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False
    
    def scan_item(self):
        """
        Attempt to identify an item using either barcode or RFID
        Returns: Item data if found, None otherwise
        """
        # Try barcode first
        barcode_result = self.barcode_scanner.scan_barcode()
        if barcode_result:
            return self.database.get_item(barcode_result['data'])
        
        # Try RFID if barcode fails
        rfid_result = self.rfid_manager.read_tag()
        if rfid_result:
            return self.database.get_item(rfid_result['tag_id'])
        
        return None
