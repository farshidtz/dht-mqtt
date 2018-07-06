# BUILD IMAGE
FROM arm32v6/python:2.7-alpine3.7 as builder


RUN apk --no-cache add git build-base

WORKDIR /home
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
	cd Adafruit_Python_DHT && \
	python setup.py install

## RUNTIME IMAGE
FROM arm32v6/python:2.7-alpine3.7

RUN apk --no-cache add ca-certificates

COPY --from=builder /usr/local/lib/python2.7 /usr/local/lib/python2.7
COPY --from=builder /home/Adafruit_Python_DHT/examples /home/examples

WORKDIR /home

ENTRYPOINT ["python", "examples/AdafruitDHT.py"]
