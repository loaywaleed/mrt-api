import RPi.GPIO as GPIO
import time

#SET GPIO MODE
GPIO.setmode(GPIO.BCM)



GPIO.setup(17,GPIO.IN)


while True:
    if GPIO.input(17) == 0:
        print("Metal detected")
    else:
        print ("No metal detected")
    
    time.sleep(0.5)

