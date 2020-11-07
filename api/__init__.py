import argparse
import asyncio
import websockets
import json

from rules import parse_rules

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

# Validate the rules

connected = set()


async def handler(websocket, path):
    raise NotImplementedError
    connected.add(websocket)
