import serial
import time
import string
import pynmea2
import csv
import datetime
import os


port = "/dev/serial0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

while True:
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()

    if newdata[0:6] == "$GPRMC":
        # if newdata[0:6] == "$GPGGA":

        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        to_csv_ = [time.time(),str(datetime.datetime.now()) , lat,lng]
        print(gps)