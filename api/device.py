class Device:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id


class Sensor(Device):
    def update_data(self):
        raise NotImplementedError


class Actuator(Device):
    def evaluate(self):
        raise NotImplementedError
