import sys
import time

print("Barcode Scanner Raw Test")
print("Please scan a barcode...")
print("(Press Ctrl+C to exit)")

try:
    while True:
        # Read one character at a time
        char = sys.stdin.read(1)
        
        # If it's a newline, that means the barcode is complete
        if char == '\n':
            print("\nBarcode complete!")
        else:
            # Print the character without a newline
            print(char, end='', flush=True)
            
        # Small delay to prevent CPU overuse
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\nTest ended by user")
