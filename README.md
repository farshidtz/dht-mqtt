# DHT-MQTT
Read humidity and temperature measurements from a DHT11/DHT22 sensor connected to a Raspberry Pi and publish them to an MQTT broker.

It also supports the AM2302 sensor, which is the wired version of DHT22.

## Run as a service
### Install
Install the [CircuitPython-DHT](https://github.com/adafruit/Adafruit_CircuitPython_DHT) library:
```bash
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```

### Configure and run as a service
1. Clone and enter the directory

```bash
git clone xxx
cd dht-mqtt
```

2. Create `config.env`

Copy from `config.env.example`.

Set the right values.

* `BROKER` (string) is the MQTT broker's host name or IP address
* `BROKER_PORT` (integer) is the MQTT broker's port
* `PIN` (integer) is the GPIO pin number that the sensor data wire port is connected to. The python board module can be used to list available pins on the board. Learn more [here](https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs/board-pins).
* `SENSOR` (string) is the sensor type. It should be either of: DHT11, DHT22, DHT21

3. Run to test:

```
./run.sh
```

3. Turn into a service

We use the `dht-mqtt.service` file to create the service.
In the service file, the path for the `run.sh` script is set to `/home/pi/dht-mqtt/run.sh`.
Modify the file to have the correct path and user.

Make a symbolic link to the service file:
```
sudo ln -s /home/pi/dht-mqtt/dht-mqtt.service /lib/systemd/system/dht-mqtt.service
```

Load the service file, enable (start on boot), and start now:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now dht-mqtt
```

Check the logs:
```bash
journalctl -u dht-mqtt -n 100 -f
```

Use `systemctl restart dht-mqtt` to load new configurations.

## Run in a Docker container
WIP

```
docker run --privileged farshidtz/adafruit_dht [11|22|2302] GPIOpin#
```

For example to read from a DHT22 attached to GPIO4:
```
docker run --privileged farshidtz/adafruit_dht 22 4

```

## Build Locally
```
docker build -t my_dht .
```
