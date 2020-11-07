import device
import json


class SensorParseError(Exception):
    """Gets raised when an invalid sensor type is passed"""
    pass

class DeviceParser:
    
    def __init__(self):
        self.devPath = '../devices/sensors.json'
        self.devDict = json.load(self.devPath)
    
    def genDevices(self):
        for key in self.devDict.keys():
            if self.devDict[key] =='motion':
                # Create an instance of a motion sensor class, passing all params from the dict
            elif self.devDict[key] == 'noise':
                pass    
            elif self.devDict[key] == 'proximity':
                pass    
            else:
                raise SensorParseError('Sensor type of {} undefined, could not parse'.format(key))
