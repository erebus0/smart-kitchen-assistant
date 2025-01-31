# src/camera/camera_manager.py

from picamera2 import Picamera2
from datetime import datetime
import os

class CameraManager:
    def __init__(self):
        self.camera = Picamera2()
        self.is_running = False
        self.image_dir = "data/images"
        
        # Create image directory if it doesn't exist
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)
        
        # Configure camera default settings
        config = self.camera.create_still_configuration()
        self.camera.configure(config)
    
    def start(self):
        """Initialize and start the camera"""
        if not self.is_running:
            self.camera.start()
            self.is_running = True
            print("Camera system initialized")
    
    def stop(self):
        """Safely stop the camera"""
        if self.is_running:
            self.camera.stop()
            self.is_running = False
            print("Camera system stopped")
    
    def capture_image(self, item_id):
        """Capture an image and save it with the item ID"""
        if not self.is_running:
            self.start()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.image_dir}/{item_id}_{timestamp}.jpg"
        
        try:
            self.camera.capture_file(filename)
            print(f"Image captured: {filename}")
            return filename
        except Exception as e:
            print(f"Error capturing image: {e}")
            return None
