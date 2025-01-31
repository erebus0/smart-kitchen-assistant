from sqlitedict import SqliteDict
from datetime import datetime
import os

class InventoryDatabase:
    def __init__(self, db_path='data/kitchen.db'):
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Initialize different tables for our database
        self.products = SqliteDict(db_path, tablename='products', autocommit=True)
        self.inventory = SqliteDict(db_path, tablename='inventory', autocommit=True)
        self.scan_history = SqliteDict(db_path, tablename='scan_history', autocommit=True)
    
    def add_product(self, barcode, name=None, category=None):
        """
        Add or update a product in the database
        If the product exists, update its information
        If it's new, create a new entry
        """
        timestamp = datetime.now().isoformat()
        
        if barcode in self.products:
            # Update existing product
            product = self.products[barcode]
            product['last_updated'] = timestamp
            if name:
                product['name'] = name
            if category:
                product['category'] = category
        else:
            # Create new product
            product = {
                'barcode': barcode,
                'name': name or 'Unknown Product',
                'category': category or 'Uncategorized',
                'added_date': timestamp,
                'last_updated': timestamp
            }
        
        self.products[barcode] = product
        return product
    
    def get_product(self, barcode):
        """Retrieve a product's information"""
        return self.products.get(barcode)
    
    def record_scan(self, barcode, scan_type='inventory_check'):
        """Record when a product is scanned"""
        timestamp = datetime.now().isoformat()
        scan_id = f"{barcode}_{timestamp}"
        
        scan_record = {
            'barcode': barcode,
            'timestamp': timestamp,
            'scan_type': scan_type,
            'product_name': self.get_product(barcode)['name'] if self.get_product(barcode) else 'Unknown'
        }
        
        self.scan_history[scan_id] = scan_record
        return scan_record

    def close(self):
        """Safely close all database connections"""
        self.products.close()
        self.inventory.close()
        self.scan_history.close()
