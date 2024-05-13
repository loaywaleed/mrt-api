import requests
import json
import time

num = 5
for i in range(50):
    num += 1
    data = {
        "voltage": num
    }
    requests.post("http://localhost:5000/api/voltage", json=data)
    print(num)
    time.sleep(0.2)
