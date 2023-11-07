import os
import time

import paho.mqtt.client as mqtt
from datetime import datetime

CLIENT_NAME = os.environ.get("CLIENT_NAME")
BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
TOPIC = os.environ.get("TOPIC")


def on_connect(client, userdata, flags, rc):
    if not rc:
        print(f'{datetime.utcnow()} | {client} connect to broker', flush=True)
    else:
        print(f'{datetime.utcnow()} | {client} not connect to broker {rc}', flush=True)


def main():
    client = mqtt.Client(CLIENT_NAME)
    client.on_connect = on_connect
    client.connect(host=BROKER_HOST, port=BROKER_PORT)
    client.loop_start()

    while True:
        time.sleep(10)
        msg = f'{datetime.utcnow()} | Temt: {20}'
        result = client.publish(TOPIC, msg)
        status = result[0]
        if status == 0:
            print(f'{datetime.utcnow()} | Publish message to topic: {TOPIC}')
        else:
            print(f'{datetime.utcnow()} | Not publish message to topic: {TOPIC}')


if __name__ == '__main__':
    main()