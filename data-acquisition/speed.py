import RPi.GPIO as GPIO
import time
import math
import requests

# GPIO setup
rpm_sensor = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(rpm_sensor, GPIO.IN, GPIO.PUD_DOWN)

sample_time =1000
maxRPM = 900
rpmMaximum = 0
pulse = 0
speed = 0
radius = 30                             #Raduis in cm

def calculate_elapse(channel):              # callback function
    global pulse, start_timer, elapse
    start_timer = 0
    pulse+=1                                # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer      # elapse for every 1 complete rotation made!
    start_timer = time.time()               # let current time equals to start_timer
   

# Function to get RPM
def getRpm():
    global count , countflag, currenttime, starttime, sample_time, countrpm, rpm_sensor
    count = 0
    countflag = False
    currenttime = 0
    starttime = int(round(time.time()*1000))

    while currenttime <= sample_time:
        if GPIO.input(rpm_sensor) == 1 :
            countflag = True
        if GPIO.input(rpm_sensor) == 0 and countflag == True:
            count += 1
            countflag = False
        currenttime = int(round(time.time()*1000)) -starttime
    countrpm = int(60000 / sample_time) * count
    # Send data to API endpoint
    # Example data to send to API

    return countrpm

# Function to display RPM, speed, and distance
def displayRpm(rpm):
    global rpmMaximum, pulse
    circ_cm = 2 * math.pi * radius  # Calculate wheel circumference in cm
    dist_m = circ_cm * (pulse / 6) / 100  # Convert distance to meters
    print(rpm, pulse)
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
