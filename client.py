import requests
import json
import time

num = 5
for i in range(100):
    num += 1
    data = {
        "voltage": num,
        "current": num * 5,
        "soc": num,
        "temp" : num,
    }
    speed = {
        "speed": num * 3,
        "rpm": num * 3 * 10,
        "distance": num * 2
    }
    blinkers = {
        "blinkers": 1,  # 0 off, 1 right, 2 left, 3 on
    }
    range_available = {
        "hours": num/10
    }
    requests.post(
        "http://127.0.0.1:5000/api/voltage_current_soc_temp", json=data)
    requests.post("http://localhost:5000/api/speed_rpm_distance", json=speed)
    requests.post(
        "http://localhost:5000/api/blinkers", json=blinkers)
    requests.post(
        "http://localhost:5000/api/range", json=range_available)
    print(num)
    time.sleep(0.1)
