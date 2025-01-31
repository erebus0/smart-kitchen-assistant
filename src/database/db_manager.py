# src/database/db_manager.py
import sqlite3
from datetime import datetime
import logging
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path="data/kitchen.db"):
        """Initialize database with all required tables"""
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        
        # Ensure data directory exists
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database and create tables
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        """Create all necessary database tables"""
        try:
            # Items table stores all kitchen items
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT UNIQUE,
                    name TEXT NOT NULL,
                    category TEXT,
                    expiry_date TEXT,
                    added_date TEXT NOT NULL,
                    quantity INTEGER DEFAULT 1,
                    minimum_quantity INTEGER DEFAULT 1,
                    image_path TEXT
                )
            ''')

            # Inventory history for tracking changes
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_id INTEGER,
                    action TEXT,
                    quantity INTEGER,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (item_id) REFERENCES items(id)
                )
            ''')

            # Shopping list table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS shopping_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_id INTEGER,
                    quantity INTEGER,
                    added_date TEXT NOT NULL,
                    priority INTEGER DEFAULT 1,
                    FOREIGN KEY (item_id) REFERENCES items(id)
                )
            ''')

            self.conn.commit()
            self.logger.info("Database setup completed successfully")
            
        except Exception as e:
            self.logger.error(f"Database setup failed: {e}")
            raise

    async def add_item(self, barcode, name, category=None, expiry_date=None, quantity=1, image_path=None):
        """Add a new item to the database"""
        try:
            current_time = datetime.now().isoformat()
            
            self.cursor.execute('''
                INSERT OR REPLACE INTO items 
                (barcode, name, category, expiry_date, added_date, quantity, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (barcode, name, category, expiry_date, current_time, quantity, image_path))
            
            item_id = self.cursor.lastrowid
            
            # Record in history
            self.cursor.execute('''
                INSERT INTO inventory_history 
                (item_id, action, quantity, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (item_id, 'add', quantity, current_time))
            
            self.conn.commit()
            return item_id
            
        except Exception as e:
            self.logger.error(f"Error adding item: {e}")
            self.conn.rollback()
            return None
