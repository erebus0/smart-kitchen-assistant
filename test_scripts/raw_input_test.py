import sys
import termios
import tty
import os

def getchar():
    # Save the current terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Change terminal settings to raw mode
        tty.setraw(sys.stdin.fileno())
        # Read a single character
        ch = sys.stdin.read(1)
    finally:
        # Restore terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Raw Input Test - Press Ctrl+C to exit")
print("Scan a barcode or type anything...")

try:
    while True:
        char = getchar()
        # Print each character and its ASCII value
        print(f"Received: '{char}' (ASCII: {ord(char)})")
except KeyboardInterrupt:
    print("\nTest ended by user")
