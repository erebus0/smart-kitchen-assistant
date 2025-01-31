# src/kitchen_assistant.py

import logging
from datetime import datetime
from src.camera.camera_handler import CameraHandler
from src.database.db_manager import DatabaseManager

class KitchenAssistant:
    def __init__(self):
        """Initialize the Kitchen Assistant with all required components"""
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/kitchen_assistant.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        try:
            self.camera = CameraManager()
            self.db = DatabaseManager()
            self.logger.info("Kitchen Assistant initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing Kitchen Assistant: {e}")
            raise

    async def start(self):
        """Start all system components"""
        try:
            self.logger.info("Starting Kitchen Assistant...")
            
            # Initialize database connection
            await self.db.connect()
            
            # Start camera system
            self.camera.start()
            
            self.logger.info("All systems started successfully")
            
        except Exception as e:
            self.logger.error(f"Error starting Kitchen Assistant: {e}")
            await self.shutdown()
            raise

    async def shutdown(self):
        """Safely shutdown all components"""
        self.logger.info("Initiating shutdown sequence...")
        
        try:
            self.camera.stop()
            await self.db.close()
            self.logger.info("Shutdown complete")
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")

    async def process_item(self, scan_type="barcode"):
        """Process a new item through either barcode or image recognition"""
        try:
            # Take photo of item
            image_path = self.camera.capture_for_barcode() if scan_type == "barcode" else self.camera.take_photo()
            
            if not image_path:
                raise Exception("Failed to capture image")

            # Process image based on type
            if scan_type == "barcode":
                result = await self.process_barcode(image_path)
            else:
                result = await self.process_image(image_path)

            return result

        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
            return None
