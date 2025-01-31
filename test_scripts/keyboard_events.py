import sys
import tty
import termios
import time

def setup_terminal():
    # Get the current terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    # Set terminal to raw mode
    tty.setraw(fd)
    return fd, old_settings

def restore_terminal(fd, old_settings):
    # Restore terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main():
    print("Barcode Scanner Test (Raw Mode)")
    print("===============================")
    print("Waiting for scan...")
    
    # Setup terminal for raw input
    fd, old_settings = setup_terminal()
    
    try:
        # Buffer to collect characters
        buffer = []
        
        while True:
            # Read a single character
            char = sys.stdin.read(1)
            
            # Convert to ASCII value
            ascii_val = ord(char)
            
            # If it's a printable character, add to buffer
            if 32 <= ascii_val <= 126:
                buffer.append(char)
                # Print progress (in raw mode, so need special handling)
                sys.stdout.write(char)
                sys.stdout.flush()
            
            # If it's a newline or carriage return, process the buffer
            elif ascii_val in [10, 13]:  # newline or carriage return
                if buffer:
                    # Convert buffer to string
                    barcode = ''.join(buffer)
                    # Print the complete barcode
                    sys.stdout.write(f"\r\nScanned: {barcode}\r\n")
                    sys.stdout.flush()
                    buffer = []  # Clear buffer for next scan
                
            # Exit on ctrl-c
            elif ascii_val == 3:
                raise KeyboardInterrupt
            
    except KeyboardInterrupt:
        print("\r\nExiting...")
    finally:
        # Always restore terminal settings
        restore_terminal(fd, old_settings)

if __name__ == "__main__":
    main()
