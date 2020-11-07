import argparse
import asyncio
import websockets
import json
import logging
import time

from rules import *
from deviceparser import DeviceParser
from devices import Device
from utils import *

logging.basicConfig(level=logging.INFO)


async def handler(websocket, path):

    async for message in websocket:
        data = json.loads(message)
        id = data['id']
        print(
            f"\nReceived message from sensor {state.device(id).ty} from id number {id[:6]} ....")

        # Dynamic service registration
        if not state.is_registered(id):
            if 'registration' in data:
                ty = data['registration']
                device = Device(id, ty)
                state.register(id, device)
            else:
                print("Message sent before registering, skipping")
                continue

        state.update_connection(id, websocket)
        if 'data' in data:
            new_data = data['data']
            state.update_data(id, new_data)

        print("\nEvaluating rules")

        rules_firing = state.rules_to_apply()
        for rule in rules_firing:

            print("Pinging ", rule.activators)

            for activator in rule.activators:
                id_to_ping = activator
                if state.is_connected(id_to_ping):
                    conn = state.get_connection(id_to_ping)
                    await conn.send(json.dumps({'id': id_to_ping, 'msg': 'instruction'}))


class SystemState:
    def __init__(self, rules, devices):
        self.rules = rules
        self.devices = devices
        self.connections = {}

    def device(self, id):
        return self.devices[id]

    def register(self, id, device):
        self.devices[id] = device

    def sensors_ids(self):
        return list(filter(lambda id: is_sensor_ty(self.devices[id].ty), self.devices.keys()))

    def actuators_ids(self):
        return list(filter(lambda id: is_actuator_ty(self.devices[id].ty), self.devices.keys()))

    def validate(self):
        act_ids = self.actuators_ids()
        sens_id = self.sensors_ids() + act_ids

        # Check that the actuator id is valid
        for r in self.rules:
            for act in r.activators:
                if not act in act_ids:
                    raise ValueError("Some rules specify invalid actuator ids")

        if not all(map(lambda r: r.statement.validate_statement(sens_id), self.rules)):
            inv_rule = filter(
                lambda r: not r.statement.validate_statement(sens_id), self.rules)
            raise ValueError("Some rules use invalid sensors ids")

    def update_connection(self, id, connection):
        self.devices[id].last_msg = time.time()
        if not id in self.connections:
            self.connections[id] = connection

    def last_msg(self, id):
        self.devices[id].last_msg

    def is_connected(self, id):
        return id in self.connections

    def is_registered(self, id):
        return id in self.devices

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

rules = parse_rules(rule_file)
# Write code to read devices here

parser = DeviceParser(device_file)
devices = parser.genDevices()

# Dictionary id to ws connection

state = SystemState(rules, devices)
state.validate()

start_server = websockets.serve(handler, 'localhost', 8765)
logging.info("\nWebsocket is initiated")
logging.info("\nServer is up and running: waiting for new messages")

evloop = asyncio.get_event_loop()
evloop.run_until_complete(start_server)
evloop.run_forever()
