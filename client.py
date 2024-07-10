import requests
import json
import time

num = 5
for i in range(100):
    num += 1
    data = {
        "voltage": num,
        "current": num * 5,
        "range": num * 10,
    }
    speed = {
        "speed": num * 3,
        "rpm": num * 3 * 10
    }
    blinkers = {
        "blinkers": 3,  # 0 off, 1 right, 2 left, 3 on
        "temperature": num,
    }
    requests.post("http://localhost:5000/api/voltage_current_soc", json=data)
    requests.post("http://localhost:5000/api/speed", json=speed)
    # requests.post(
    #     "http://localhost:5000/api/blinkers_temperature", json=blinkers)

    print(num)
    time.sleep(2)
