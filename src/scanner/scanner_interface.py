# src/scanner/scanner_interface.py
from evdev import InputDevice, categorize, ecodes
import asyncio
import sys
from ..database.inventory_db import InventoryDatabase

class BarcodeScanner:
    def __init__(self, device_path='/dev/input/event0'):
        self.device_path = device_path
        self.db = InventoryDatabase()
        self.scanner = InputDevice(device_path)

    async def get_user_input(self, prompt):
        """Get user input asynchronously"""
        loop = asyncio.get_event_loop()
        print(prompt)
        return await loop.run_in_executor(None, input)

	async def process_scan(self, db):  # Add 'db' parameter
    while True:
        barcode = await self.read_barcode()
        db.record_scan(barcode) 

    async def handle_barcode(self, barcode):
        """Handle scanned barcode"""
        print(f"\nScanned Barcode: {barcode}")
        
        product = self.db.get_product(barcode)
        if product:
            print(f"Product found: {product['name']}")
            action = await self.get_user_input("\nWhat would you like to do?\n1. Update quantity\n2. View details\nChoice (1/2): ")
            
            if action == '1':
                qty = await self.get_user_input("Enter new quantity: ")
                # Update quantity logic here
        else:
            add_new = await self.get_user_input("New product! Add details? (y/n): ")
            if add_new.lower() == 'y':
                name = await self.get_user_input("Enter product name: ")
                category = await self.get_user_input("Enter category: ")
                self.db.add_product(barcode, {'name': name, 'category': category})

    async def process_scan(self):
        """Main scanning loop"""
        print("Barcode Scanner Ready")
        print("Commands:")
        print("'q' - Quit")
        print("'n' - Add/Update product name")
        print("'i' - View inventory")
        print("'l' - Generate low stock list")
        
        buffer = []
        
        try:
            async for event in self.scanner.async_read_loop():
                if event.type == ecodes.EV_KEY and event.value == 1:
                    if event.code == ecodes.KEY_ENTER:
                        barcode = ''.join(buffer)
                        if barcode:
                            await self.handle_barcode(barcode)
                        buffer = []
                    else:
                        key_lookup = self.scanner.capabilities()[ecodes.EV_KEY]
                        for code in key_lookup:
                            if code == event.code:
                                char = ecodes.KEY[event.code].replace('KEY_', '')
                                buffer.append(char)
        except KeyboardInterrupt:
            print("\nScanner stopped.")

    def close(self):
        """Clean up resources"""
        self.db.close()
