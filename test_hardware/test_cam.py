# test_cam.py
from picamera2 import Picamera2
import time

def main():
    try:
        print("Available camera devices:")
        import subprocess
        subprocess.run(["ls", "-l", "/dev/video*"])
        
        print("\nInitializing Picamera2...")
        picam2 = Picamera2()
        
        print("Camera configurations available:")
        print(picam2.sensor_modes)
        
        print("\nConfiguring camera...")
        config = picam2.create_still_configuration()
        picam2.configure(config)
        
        print("Starting camera...")
        picam2.start()
        time.sleep(2)  # Warm-up
        
        print("Capturing image...")
        picam2.capture_file("test_picture.jpg")
        print("Image saved as test_picture.jpg")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nDiagnostic information:")
        try:
            print("\nChecking libcamera:")
            subprocess.run(["libcamera-hello", "--list-cameras"])
        except:
            print("libcamera-hello not available")
            
    finally:
        try:
            picam2.stop()
        except:
            pass

if __name__ == "__main__":
    main()
