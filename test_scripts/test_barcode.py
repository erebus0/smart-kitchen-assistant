print("Barcode Scanner Test")
print("Please scan a barcode (or type 'exit' to quit)")

while True:
    # Wait for input from the scanner
    # The scanner works like a keyboard, so we use input()
    barcode = input("Waiting for scan: ")
    
    # If someone types 'exit', stop the program
    if barcode.lower() == 'exit':
        break
    
    # Show what was scanned
    print(f"Scanned barcode: {barcode}")
    print("Scan another barcode or type 'exit' to quit")
