import asyncio
from src.scanner.scanner_interface import BarcodeScanner
from src.database.inventory_db import InventoryDatabase
from src.web.app import WebServer  # Add web server import

class KitchenAssistant:
    def __init__(self):
        self.db = InventoryDatabase()
        self.scanner = BarcodeScanner('/dev/input/event0')
        self.web_server = WebServer(self.db)  # Initialize web server

    async def start(self):
        print("\nKitchen Assistant Starting...")
        print("===========================")
        
        try:
            print("Initializing Components:")
            print("- Starting web interface...")
            self.web_server.start()  # Start Flask server
            
            print("- Activating barcode scanner...")
            await self.scanner.process_scan(self.db)  # Pass db reference
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
            print("Shutdown complete.")

def main():
    assistant = KitchenAssistant()
    asyncio.run(assistant.start())

if __name__ == "__main__":
    main()
