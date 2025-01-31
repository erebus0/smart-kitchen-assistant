# src/barcode/barcode_processor.py
import cv2
from pyzbar.pyzbar import decode
import logging
from pathlib import Path

class BarcodeProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def process_image(self, image_path):
        """Process an image to detect and decode barcodes"""
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Failed to load image: {image_path}")

            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect barcodes
            barcodes = decode(gray)
            
            results = []
            for barcode in barcodes:
                result = {
                    'type': barcode.type,
                    'data': barcode.data.decode('utf-8'),
                    'rect': barcode.rect,
                    'polygon': barcode.polygon
                }
                results.append(result)

            return results

        except Exception as e:
            self.logger.error(f"Error processing barcode image: {e}")
            return None

    async def save_barcode_image(self, image_path, barcode_data):
        """Save a processed image with barcode markers"""
        try:
            image = cv2.imread(image_path)
            
            # Draw rectangles around detected barcodes
            for barcode in barcode_data:
                rect = barcode['rect']
                x, y, w, h = rect.left, rect.top, rect.width, rect.height
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Save marked image
            output_path = str(Path(image_path).with_suffix('.processed.jpg'))
            cv2.imwrite(output_path, image)
            return output_path

        except Exception as e:
            self.logger.error(f"Error saving processed barcode image: {e}")
            return None
