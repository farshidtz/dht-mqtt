# DHT-MQTT
Read humidity and temperature measurements from an DHT11/DHT22/AM2302 sensor and publish them to an MQTT broker.

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

2. Update `config.env`
Set the right values.

3. Run to test:
```
./run.sh
```

3. Turn into a service
We use the `dht-mqtt.service` file to create the service.
In the service file, the path for the `run.sh` script is set to `/home/pi/dht-mqtt/run.sh`.
Modify the file to have the correct paths and user.

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
