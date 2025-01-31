from src.kitchen_controller import KitchenController
import time

def test_kitchen_assistant():
    print("Testing Kitchen Assistant Integration")
    controller = KitchenController()
    
    try:
        # Start all systems
        controller.start()
        print("\nKitchen Assistant is ready!")
        print("Options:")
        print("1. Add new item")
        print("2. Scan existing item")
        print("3. Exit")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                # Simulate adding new item
                name = input("Enter item name: ")
                expiry = input("Enter expiry date (YYYY-MM-DD) or press Enter to skip: ")
                
                # In real implementation, this would scan barcode/RFID
                id_number = input("Enter test ID number: ")
                
                if controller.add_item(id_number, name, expiry if expiry else None):
                    print("Item added successfully!")
                else:
                    print("Failed to add item")
                    
            elif choice == "2":
                # Simulate scanning item
                print("Scanning for item...")
                item = controller.scan_item()
                if item:
                    print(f"Found item: {item['name']}")
                else:
                    print("No item found")
                    
            elif choice == "3":
                break
                
    finally:
        controller.stop()

if __name__ == "__main__":
    test_integration()
