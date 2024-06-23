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
        "speed" : num * 5,
    }
    requests.post("http://localhost:5000/api/voltage_current_range", json=data)
    requests.post("http://localhost:5000/api/speed", json=speed)
    print(num)
    time.sleep(1)
