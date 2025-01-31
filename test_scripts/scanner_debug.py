import sys
import time
from datetime import datetime

def debug_scanner():
    print("=== Scanner Debug Mode ===")
    print("This will show every character received, including special characters")
    print("When you scan a barcode, you should see each character appear")
    print("Press Ctrl+C to exit\n")

    buffer = []
    try:
        while True:
            # Read a single character
            char = sys.stdin.read(1)
            
            # Get ASCII value of the character
            ascii_val = ord(char)
            
            # Print detailed information about what we received
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] Received: '{char}' (ASCII: {ascii_val})")
            
            # Add to our buffer
            buffer.append(char)
            
            # If we get a newline or carriage return, show the complete barcode
            if char in '\n\r':
                barcode = ''.join(buffer)
                print(f"\n>>> Complete barcode: {barcode}")
                print(f">>> Length: {len(barcode)} characters\n")
                buffer = []  # Reset buffer for next scan
            
            # Ensure output is displayed immediately
            sys.stdout.flush()
            
    except KeyboardInterrupt:
        print("\nExiting debug mode...")
        if buffer:
            print(f"Partial buffer contents: {''.join(buffer)}")

if __name__ == "__main__":
    debug_scanner()
