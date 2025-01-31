from pyzbar.pyzbar import decode
import cv2
import numpy as np

class BarcodeScanner:
    def __init__(self, camera_manager):
        self.camera = camera_manager

    def scan_barcode(self, save_debug_image=False):
        """
        Attempt to scan a barcode using the camera
        Returns: The barcode data if found, None otherwise
        """
        # Capture image from camera
        image = self.camera.capture_image()
        if image is None:
            return None

        # Convert to grayscale for better barcode detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Save debug image if requested
        if save_debug_image:
            cv2.imwrite('data/images/debug_scan.jpg', gray)

        # Try to decode any barcodes in the image
        barcodes = decode(gray)
        
        # Return the first barcode found
        if barcodes:
            return {
                'data': barcodes[0].data.decode('utf-8'),
                'type': barcodes[0].type
            }
        
        return None
