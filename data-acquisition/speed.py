import RPi.GPIO as GPIO
import time
import math
import requests

# GPIO setup
rpm_sensor = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(rpm_sensor, GPIO.IN, GPIO.PUD_DOWN)

# Constants and variables
radius = 30  # Radius in cm
pulse = 0
rpmMaximum = 0

# Callback function for GPIO event
def calculate_elapse(channel):
    global pulse
    pulse += 1

# Function to get RPM
def getRpm():
    global pulse
    return pulse * (60 / 6)

# Function to display RPM, speed, and distance
def displayRpm(rpm):
    global rpmMaximum, pulse
    circ_cm = 2 * math.pi * radius  # Calculate wheel circumference in cm
    dist_m = circ_cm * (pulse / 6) / 100  # Convert distance to meters
    speed_kmh = rpm * (circ_cm / 100000) * 60 * 60  # Calculate speed in km/h

    print(f"RPM: {rpm:.0f}, Speed: {speed_kmh:.2f} km/h, Distance: {dist_m:.2f} m")

    # Example data to send to API
    data = {
        "speed": round(speed_kmh, 2),
        "rpm": round(rpm),
        "distance": round(dist_m / 1000, 2),  # Convert distance to kilometers
    }

    # Send data to API endpoint
    try:
        response = requests.post("http://localhost:5000/api/speed_rpm_distance", json=data)
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

# GPIO event detection
GPIO.add_event_detect(rpm_sensor, GPIO.FALLING, callback=calculate_elapse, bouncetime=20)

# Main loop
try:
    while True:
        rpm = getRpm()
        if rpm > rpmMaximum:
            rpmMaximum = rpm
        displayRpm(rpm)
        time.sleep(1)  # Adjust sleep time as needed
except KeyboardInterrupt:
    print("Measurement stopped by user")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
