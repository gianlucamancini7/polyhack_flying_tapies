import json
import devices


class DeviceParser:

    def __init__(self, path):
        self.devices = json.load(open(path, 'rb'))



    def genDevices(self):
        res = {}
        for device in self.devDict.keys():
            res[device['id']] = Device(device['id'], device['type'])
        return res
