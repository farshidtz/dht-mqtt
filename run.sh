#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

# Load environment variables from env file
set -o allexport
source $DIR/config.env set
set +o allexport

python -u $DIR/dht-mqtt.py
