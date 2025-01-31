from src.database.db_manager import KitchenDatabase

def test_database():
    print("Testing database functionality...")
    
    # Initialize database
    db = KitchenDatabase()
    
    # Test adding an item
    test_barcode = "5901234123457"
    try:
        db.add_item(test_barcode, "Test Product")
        print("✓ Successfully added test item")
        
        # Retrieve the item
        item = db.get_item(test_barcode)
        if item and item['name'] == "Test Product":
            print("✓ Successfully retrieved test item")
        else:
            print("✗ Failed to retrieve test item")
            
    except Exception as e:
        print(f"✗ Error during database test: {e}")
    
    finally:
        db.close()

if __name__ == "__main__":
    test_database()
