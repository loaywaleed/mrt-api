import serial
import time
import requests

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
                    latitude = data[3]  # Latitude
                    lat_direction = data[4]  # Latitude direction (N/S)
                    longitude = data[5]  # Longitude
                    lon_direction = data[6]  # Longitude direction (E/W)
                    print(f"Latitude: {latitude} {lat_direction}")
                    print(f"Longitude: {longitude} {lon_direction}")

                    # Prepare data for API
                    data = {
                        "latitude": latitude,
                        "longitude": longitude
                    }

                    # Send data to API endpoint
                    try:
                        response = requests.post("http://localhost:5000/api/gps", json=data)
                        if response.status_code == 200:
                            print("Data sent successfully")
                        else:
                            print(f"Failed to send data: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error sending data: {e}")
            
            time.sleep(0.5)  # Small delay to prevent overwhelming the CPU
    
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        ser.close()

if __name__ == "__main__":
    read_from_serial()
