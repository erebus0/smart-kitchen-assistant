import sys
import select
import time

def test_scanner():
    print("Scanner Test - Waiting for barcode...")
    print("(Press Ctrl+C to exit)")
    
    # Buffer for collecting input
    input_buffer = []
    
    while True:
        # Check if there's any input available
        if select.select([sys.stdin], [], [], 0.1)[0]:
            # Read one character
            char = sys.stdin.read(1)
            
            # If it's a special character, print its ASCII value
            if ord(char) < 32:
                print(f"Special character received: ASCII {ord(char)}")
            else:
                input_buffer.append(char)
                print(f"Character received: {char}")
            
            # If we get a termination character (like Enter)
            if char in '\n\r':
                if input_buffer:
                    complete_input = ''.join(input_buffer)
                    print(f"\nComplete input: {complete_input}")
                input_buffer = []  # Reset buffer
        
        # Small delay to prevent CPU overuse
        time.sleep(0.01)

try:
    test_scanner()
except KeyboardInterrupt:
    print("\nTest ended by user")
