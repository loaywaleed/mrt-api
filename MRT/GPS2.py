import serial
import time
import string
import pynmea2
import csv
import datetime
import os

def append_to_csv():
    with open ("/home/pi/Desktop/results/GPS.csv"
        , mode='a+' ) as sensor_readings:
        sensor_write = csv.writer(sensor_readings)
        append_to_log = sensor_write.writerow(to_csv_)
        return(append_to_log)
def append_to_csv_():
    with open ("/home/pi/Desktop/results/GPSd.csv"
        , mode='a+' ) as sensor_readings:
        sensor_write = csv.writer(sensor_readings)
        append_to_log = sensor_write.writerow(to_csv_)
        return(append_to_log)
try:
    os.system('sudo rm /home/pi/Desktop/results/GPSd.csv')
except:
    Exception


while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
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
        append_to_csv()
        append_to_csv_()