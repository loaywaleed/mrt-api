import serial
import time

def read_from_serial():
    port = "/dev/serial0"  # Change this if your port is different
    baud_rate = 9600  # GPS modules typically use 9600 baud rate

    # Open the serial port
    ser = serial.Serial(port, baud_rate, timeout=1)
    
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('ascii', errors='replace').strip()
                print(data)
            time.sleep(0.5)  # Small delay to prevent overwhelming the CPU
    
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        ser.close()

if __name__ == "__main__":
    read_from_serial()
