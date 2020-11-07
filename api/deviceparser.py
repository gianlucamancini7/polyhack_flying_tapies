import json


class SensorParseError(Exception):
    """Gets raised when an invalid sensor type is passed"""
    pass


class DeviceParser:

    def __init__(self, path):
        self.devDict = json.load(open(path, 'rb'))

    def genDevices(self):
        res = {}
        for key in self.devDict.keys():
            value = self.devDict[key]
            id = value['id']
            ty = value['type']
            if ty == 'motion':
                res[id] = {'id': id, 'data': [], 'ty': 'motion'}
            elif ty == 'noise':
                res[id] = {'id': id, 'data': [], 'ty': 'noise'}
            elif ty == 'proximity':
                res[id] = {'id': id, 'data': [], 'ty': 'proximity'}
            else:
                raise SensorParseError(
                    'Sensor type of {} undefined, could not parse'.format(key))
        return res
