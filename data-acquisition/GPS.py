import serial
import time

def knots_to_kmh(speed_knots):
    # 1 knot = 1.852 km/hr
    return float(speed_knots) * 1.852

def read_from_serial():
    port = "/dev/serial0"  # Change this if your port is different
    baud_rate = 9600  # GPS modules typically use 9600 baud rate

    # Open the serial port
    ser = serial.Serial(port, baud_rate, timeout=1)
    
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('ascii', errors='replace').strip().split(',')
                if data[0] == '$GPRMC' and data[2] == 'A':  # Check for valid data (A = valid, V = void)
                    utc_time = data[1]  # UTC time
                    latitude = data[3]  # Latitude
                    lat_direction = data[4]  # Latitude direction (N/S)
                    longitude = data[5]  # Longitude
                    lon_direction = data[6]  # Longitude direction (E/W)
                    speed_knots = data[7]  # Speed in knots
                    
                    # Convert speed from knots to km/hr
                    speed_kmh = knots_to_kmh(speed_knots)
                    
                    # Print UTC time, latitude, longitude, and speed in km/hr
                    print(f"UTC Time: {utc_time}")
                    print(f"Latitude: {latitude} {lat_direction}")
                    print(f"Longitude: {longitude} {lon_direction}")
                    print(f"Speed: {speed_kmh:.2f} km/hr")
                    
            time.sleep(0.5)  # Small delay to prevent overwhelming the CPU
    
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        ser.close()

if __name__ == "__main__":
    read_from_serial()
