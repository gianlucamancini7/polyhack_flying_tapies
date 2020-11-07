import device
import json


class SensorParseError(Exception):
    """Gets raised when an invalid sensor type is passed"""
    pass

class DeviceParser:
    
    def __init__(self, path):
        self.devPath = '../devices/sensors.json'
        self.devDict = json.load(path)
    
    def genDevices(self):
        for key in self.devDict.keys():
            if self.devDict[key] =='motion':
                passs
            elif self.devDict[key] == 'noise':
                pass    
            elif self.devDict[key] == 'proximity':
                pass    
            else:
                raise SensorParseError('Sensor type of {} undefined, could not parse'.format(key))
