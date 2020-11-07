import asyncio
import websockets
import logging
import json
import argparse

from sensors import Sensor
from actuators import Actuator


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='API for ASUS Challenge')
    parser.add_argument(
        'device_file', help='File where the devices are stored in JSON format')

    args = parser.parse_args()
    device_file = args.device_file

    # Parse here

    logging.basicConfig()

    sensors = []
    actuators = []
    evloop = asyncio.get_event_loop()
    for sensor in sensors:
        evloop.run_in_executor(sensor.start_listen())

    for act in actuators:
        evloop.run_in_executor(act.start_listen())

    evloop.run_forever()
