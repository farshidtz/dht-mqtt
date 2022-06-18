# SPDX-FileCopyrightText: 2022 Farshid Tavakolizadeh
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# RUN:
# BROKER=localhost python read.py

import time
import board
import adafruit_dht
import requests
import os
import paho.mqtt.client as paho

broker=os.environ['BROKER']
port=os.environ['BROKER_PORT']
pin=os.environ['PIN']
sensor=os.environ['SENSOR']

# Initialize the sensor at the given pin:
dhtDevice = getattr(adafruit_dht, sensor)(pin)

# Initialize the MQTT client
mqtt_client=paho.Client(client_id="pluto-dht22")

def on_connect(client, userdata, flags, rc):
    print("Connected: {}".format(paho.connack_string(rc)))

def on_disconnect(client, userdata, rc):
    print("Disonnected: {}".format(paho.connack_string(rc)))

mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.connect_async(broker,int(port))
mqtt_client.loop_start()

while True:
    try:
        #print("----------------------------")
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f}C  Humidity: {}% ".format(temperature, humidity))

        rc,_=mqtt_client.publish("pluto/dht22/temperature", temperature, retain=True)
        if rc != 0:
            print("Publish temperature error: {}".format(paho.error_string(rc)))

        rc,_=mqtt_client.publish("pluto/dht22/humidity", humidity, retain=True)
        if rc != 0:
            print("Publish humidity error: {}".format(paho.error_string(rc)))


    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        mqtt_client.loop_stop()
        raise error

    time.sleep(60.0)

