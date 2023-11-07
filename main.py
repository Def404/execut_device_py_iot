import os
import time

import paho.mqtt.client as mqtt
from datetime import datetime

CLIENT_NAME = os.environ.get("CLIENT_NAME")
BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
TOPIC = os.environ.get("TOPIC")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if not rc:
        print(f'{datetime.utcnow()} | {client} connect to broker', flush=True)
    else:
        print(f'{datetime.utcnow()} | {client} not connect to broker {rc}', flush=True)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def main():
    while True:
        try:
            client = mqtt.Client(CLIENT_NAME)
            client.on_connect = on_connect

            client.connect(host=BROKER_HOST, port=BROKER_PORT)


            message = f'{CLIENT_NAME}: {20}'
            result = client.publish(TOPIC, message)

            if not result[0]:
                print(f'{datetime.utcnow()} message is publish')
            else:
                print(f'{datetime.utcnow()} message is not publish')

            client.disconnect()
        finally:
            print(f'{datetime.utcnow()} | error')
            time.sleep(5)
            main()

        time.sleep(10)


if __name__ == '__main__':
    main()