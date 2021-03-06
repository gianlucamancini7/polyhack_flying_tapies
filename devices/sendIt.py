import asyncio
import websockets
import logging
import json
import argparse
import time

from sensors import Sensor
from actuators import Actuator
from deviceparser import DeviceParser
from utils import *

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='API for ASUS Challenge')
    parser.add_argument(
        'device_file', help='File where the devices are stored in JSON format')

    args = parser.parse_args()
    device_file = args.device_file

    parser = DeviceParser(device_file)
    devices = parser.genDevices()

    logging.info(
        "\nIOT fleet is deployed in Hackwill: devices are ready to send measurements to the API")

    sensors = []
    actuators = []

    for id, ty in devices.items():
        if is_sensor_ty(ty):
            sensors.append(Sensor(id, ty))
        elif is_actuator_ty(ty):
            actuators.append(Actuator(id, ty))
        else:
            raise ValueError("Not a sensors or acutator")

    sensors_tasks = [s.start_listen() for s in sensors]
    actuators_tasks = [a.start_listen() for a in actuators]
    tasks = sensors_tasks + actuators_tasks
    loop = asyncio.get_event_loop()
    cors = asyncio.wait(tasks)
    loop.run_until_complete(cors)
