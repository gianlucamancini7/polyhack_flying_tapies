import json


class DeviceParser:

    def __init__(self, path):
        self.devices = json.load(open(path, 'rb'))

    def genDevices(self):
        res = {}
        for device in self.devices:
            res[device['id']] = device['type']
        return res
