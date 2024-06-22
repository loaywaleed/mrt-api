import requests
import json
import time

num = 5
for i in range(50):
    num += 1
    data = {
        "voltage": num,
        "current": num * 5
    }
    requests.post("http://localhost:5000/api/voltage_current_range", json=data)
    print(num)
    time.sleep(1)
