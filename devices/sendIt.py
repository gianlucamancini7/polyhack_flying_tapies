import asyncio
import websockets
import logging
import json
import argparse

from sensors import Sensor
from actuators import Actuator
from deviceparser import DeviceParser
from utils import *

if __name__ == "__main__":
    logging.basicConfig()

    parser = argparse.ArgumentParser(description='API for ASUS Challenge')
    parser.add_argument(
        'device_file', help='File where the devices are stored in JSON format')

    # TODO: remove after debug
    parser.add_argument(
        'rules', help='File where the devices are stored in JSON format')

    args = parser.parse_args()
    device_file = args.device_file

    parser = DeviceParser(device_file)
    devices = parser.genDevices()

    sensors = []
    actuators = []

    for id, ty in devices.items():
        if is_sensor_ty(ty):
            sensors.append(Sensor(id, ty))
        elif is_actuator_ty(ty):
            actuators.append(Actuator(id, ty))
        else:
            raise ValueError("Not a sensors or acutator")

    evloop = asyncio.get_event_loop()
    for sensor in sensors:
        evloop.run_in_executor(sensor.start_listen())

    for act in actuators:
        evloop.run_in_executor(act.start_listen())

    evloop.run_forever()
