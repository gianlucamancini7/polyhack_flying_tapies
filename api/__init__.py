import argparse
import asyncio
import websockets
import json

from rules import *


async def handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        id = data['id']
        state.update_connection(id, websocket)
        if 'data' in data:
            state.update_data(id, data['data'])
        rules_firing = state.rules_to_apply()
        for rule in rules_firing:
            id_to_ping = rule.activator.id
            conn = state.get_connection(id_to_ping)
            await conn.send(json.dumps({'id': id_to_ping, 'msg': 'something'}))


class SystemState:
    def __init__(self, rules, devices, connections):
        self.rules = rules
        self.devices = devices
        self.connections = rules

    def update_connection(self, id, connection):
        if not id in self.connections:
            self.connections[id] = connection

    def get_connection(self, id):
        return self.connections[id]

    def data(self, id):
        return self.devices[id].data

    def update_data(self, id, new_data):
        self.devices[id].data = new_data

    def rules_to_apply(self):
        return filter(lambda r: r.statement.evaluate(self), self.rules)


parser = argparse.ArgumentParser(description='API for ASUS Challenge')
parser.add_argument(
    'rule_file', help='File where the rules are stored in pickle format')
parser.add_argument(
    'device_file', help='File where the devices are stored in JSON format')

args = parser.parse_args()
rule_file = args.rule_file
device_file = args.device_file

rules = parse_rules(rule_file)
# Write code to read devices here
devices = {}

# Validate the rules

# Dictionary id to ws connection
connections = {}

state = SystemState(rules, devices, connections)

start_server = websockets.serve(handler, 'localhost', 8765)

evloop = asyncio.get_event_loop()
evloop.run_until_complete(start_server)
evloop.run_forever()
