# Original script from https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

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

broker = os.environ['BROKER']
port=1883

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

mqtt_client=paho.Client("pluto-dht22")

while True:
    mqtt_client.connect(broker,port)

    while True:
        try:
            print("----------------------------")
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp: {:.1f}C  Humidity: {}% ".format(temperature, humidity))

            ret=mqtt_client.publish("pluto/dht22/temperature", temperature)
            print("Published temperature. Client returned: {}".format(ret))

            ret=mqtt_client.publish("pluto/dht22/humidity", humidity)
            print("Published humidity. Client returned: {}".format(ret))


        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(60.0)

    time.sleep(10.0)
