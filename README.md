# Adafruit_Python_DHT_Docker
Dockerized [Adafruit Python DHT Sensor Library](https://github.com/adafruit/Adafruit_Python_DHT) for Raspberry Pi

## Run 
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
