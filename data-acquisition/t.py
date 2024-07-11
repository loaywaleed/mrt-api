import RPi.GPIO as GPIO
import time
import math
import requests


rpm_sensor = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(rpm_sensor, GPIO.IN,GPIO.PUD_DOWN)

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

def getRpm() :
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
    countrpm = int(60000/sample_time)*count
    # Send data to API endpoint
    # Example data to send to API

    return countrpm

def displayRpm(Rpm):
    global rpmMaximum, pulse, speed,distanceX
        
    circ_cm = (2 * math.pi) * radius          # calculate wheel circumference in CM
    dist_km = circ_cm / 100000            # convert cm to km
    km_per_sec = dist_km * (Rpm / 60)      # calculate KM/sec
    speed = km_per_sec * 3600           # calculate KM/h
    rotation = pulse / 6
    distance = (dist_km*rotation)*1000    # measure distance traverse in meter
    distanceX= distance
    data = {
        "speed": round(speed, 2),
        "rpm": round(Rpm),
        "distance": round(distance / 1000, 2),  # Convert distance to kilometers
    }
    try:
        response = requests.post("http://localhost:5000/api/speed_rpm_distance", json=data)
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

    
    print('RPM: {0:.0f}- speed:{1:.0f}-KMH Distance:{2:.2f}m pulse:{3}'.format(Rpm, speed, distance, pulse))

#    print("maximum RPM is ",rpmMaximum)
GPIO.add_event_detect(rpm_sensor, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)


while True :
    rpm = getRpm()/6


    if rpm > rpmMaximum :
        rpmMaximum = rpm
    displayRpm(rpm)

    time.sleep(0.0000001)