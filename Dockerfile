FROM resin/rpi-raspbian


RUN apt update && apt -y install git build-essential python-dev

WORKDIR /home
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
	cd Adafruit_Python_DHT && \
	sudo python setup.py install


ENTRYPOINT ["python", "Adafruit_Python_DHT/examples/AdafruitDHT.py"]
