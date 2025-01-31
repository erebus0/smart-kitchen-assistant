from evdev import InputDevice, categorize, ecodes
import asyncio
import sys

async def monitor_device(device_path):
    print(f"Monitoring device: {device_path}")
    print("Waiting for barcode scan...")
    print("(Press Ctrl+C to exit)")
    
    # Open the input device
    device = InputDevice(device_path)
    
    # Buffer to collect characters
    buffer = []
    
    async for event in device.async_read_loop():
        if event.type == ecodes.EV_KEY:
            # Only handle key press events (ignore key release)
            if event.value == 1:  # Key press
                # Convert key code to character
                if event.code == ecodes.KEY_ENTER:
                    # Process complete barcode
                    barcode = ''.join(buffer)
                    print(f"\nScanned Barcode: {barcode}")
                    buffer = []  # Reset buffer
                else:
                    # Get the character for this key
                    key_lookup = device.capabilities()[ecodes.EV_KEY]
                    for code in key_lookup:
                        if code == event.code:
                            char = ecodes.KEY[event.code].replace('KEY_', '')
                            buffer.append(char)
                            print('.', end='', flush=True)  # Show progress

async def find_scanner():
    # List all input devices
    from evdev import list_devices
    devices = [InputDevice(path) for path in list_devices()]
    
    print("Available input devices:")
    for device in devices:
        print(f"  {device.path}: {device.name}")
        if "HIDKeyBoard" in device.name:  # Match your scanner's name
            return device.path
    
    return None

async def main():
    scanner_path = await find_scanner()
    if scanner_path:
        try:
            await monitor_device(scanner_path)
        except PermissionError:
            print("\nPermission denied. Try running with sudo:")
            print(f"sudo python3 {sys.argv[0]}")
    else:
        print("No barcode scanner found!")

if __name__ == "__main__":
    asyncio.run(main())
