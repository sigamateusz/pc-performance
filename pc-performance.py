import time

import psutil
import requests
import schedule

API_KEY = 'ORANQWHYII2DI4PL'
URL = "https://api.thingspeak.com/update"


def send_req(cpu, ram):
    params = {'api_key': API_KEY, 'field1': cpu, 'field2': ram}
    requests.get(url=URL, params=params)


def job():
    cpu = psutil.cpu_percent()
    print(f"cpu: {cpu}%")
    ram = psutil.virtual_memory().percent
    print(f"ram: {ram}%")
    print("-----------------------------")
    send_req(cpu, ram)


schedule.every(1).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
