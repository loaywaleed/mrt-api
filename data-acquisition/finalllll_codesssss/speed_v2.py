#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import math
import requests


# Pin setup
sensor_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Variables
counter = 0
total_revolutions = 0

last_time = time.time()
last_state = GPIO.input(sensor_pin)
interval = 1  # 1 second interval for RPM calculation
wheel_diameter = 0.6  # in meters

def calculate_speed(rpm):
    # Calculate speed in m/s
    wheel_circumference = wheel_diameter * 3.14159
    speed_m_s = (rpm * wheel_circumference) / 60  # Speed in m/s
    # Convert speed to km/h
    speed_km_h = speed_m_s * 3.6
    return speed_km_h

def calculate_distance(revolutions):
    # Calculate distance in meters
    wheel_circumference = wheel_diameter * 3.14159
    distance_m = revolutions * wheel_circumference
    return distance_m

# Function to display RPM, speed, and distance
def display(rpm, revolutions):
    print(revolutions)
    distance_m = calculate_distance(revolutions)
    distance_km = distance_m / 1000  # Convert to kilometers

    speed_kmh = calculate_speed(rpm)  # Calculate speed in km/h
    print(f"RPM: {rpm:.0f}, Speed: {speed_kmh:.2f} km/h, distance: {distance_m:.2f} m")
    # Example data to send to API
    data = {
        "speed": round(speed_kmh, 2),
        "rpm": round(rpm),
        "distance": round(distance_m, 2),
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


try:
    while True:
        current_time = time.time()
        current_state = GPIO.input(sensor_pin)

        # Detect a rising edge (low to high transition)
        if last_state == GPIO.LOW and current_state == GPIO.HIGH:
            counter += 1
            total_revolutions += 1

        # Calculate and print RPM and speed every second
        if (current_time - last_time) >= interval:
            rpm = (counter / interval) * 60  # Convert to RPM

            # print(f"RPM: {rpm}")

            # speed_km_h = calculate_speed(rpm)
            # print(f"Speed: {speed_km_h} km/h")

            display(rpm, total_revolutions)

            counter = 0  # Reset counter
            last_time = current_time

        last_state = current_state  # Update last state
        time.sleep(0.01)  # Short delay to prevent high CPU usage

except KeyboardInterrupt:
    print("Measurement stopped by user")

finally:
    GPIO.cleanup()
