import argparse
import asyncio
import websockets
import json
import logging

from rules import *
from deviceparser import DeviceParser
from utils import *

logging.basicConfig()


async def handler(websocket, path):
    print(websocket)
    async for message in websocket:
        data = json.loads(message)
        id = data['id']
        print("Received message from ", id)
        state.update_connection(id, websocket)
        if 'data' in data:
            new_data = data['data']
            state.update_data(id, new_data)
            print("Updating data of ", id, " to ", new_data)

        print("Evaluating rules")
        rules_firing = state.rules_to_apply()
        for rule in rules_firing:
            print("Pinging ", rule.activators)
            for activator in rule.activators:
                id_to_ping = activator.id
                conn = state.get_connection(id_to_ping)
                await conn.send(json.dumps({'id': id_to_ping, 'msg': 'instruction'}))


class SystemState:
    def __init__(self, rules, devices):
        self.rules = rules
        self.devices = devices
        self.connections = {}

    def sensors_ids(self):
        return filter(lambda id: is_sensor_ty(self.devices[id]['ty']), self.devices.keys())

    def actuators_ids(self):
        return filter(lambda id: is_actuator_ty(self.devices[id]['ty']), self.devices.keys())

    def validate(self):
        act_ids = self.actuators_ids()
        sens_id = self.sensors_ids()

        # Check that the actuator id is valid
        if not all(map(lambda r: r.activator in act_ids, self.rules)):
            raise ValueError("Some rules specify invalid actuator ids")

        if not all(map(lambda r: r.validate_statement(sens_id), self.rules)):
            raise ValueError("Some rules use invalid sensors ids")

    def update_connection(self, id, connection):
        if not id in self.connections:
            self.connections[id] = connection

    def get_connection(self, id):
        return self.connections[id]

    def data(self, id):
        return self.devices[id].getData()

    def update_data(self, id, new_data):
        self.devices[id].setData(new_data)

    def rules_to_apply(self):
        return filter(lambda r: r.statement.evaluate(self), self.rules)


parser = argparse.ArgumentParser(description='API for ASUS Challenge')
parser.add_argument(
    'device_file', help='File where the devices are stored in JSON format')
parser.add_argument(
    'rule_file', help='File where the rules are stored in pickle format')


args = parser.parse_args()
rule_file = args.rule_file
device_file = args.device_file

rules = []  # parse_rules(rule_file)
# Write code to read devices here

parser = DeviceParser(device_file)
devices = parser.genDevices()

# Dictionary id to ws connection

state = SystemState(rules, devices)
state.validate()

start_server = websockets.serve(handler, 'localhost', 8765)

evloop = asyncio.get_event_loop()
evloop.run_until_complete(start_server)
evloop.run_forever()
