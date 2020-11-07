class Device:
    def __init__(self, id, connection):
        self.id = id
        self.connection = connection

    def get_id(self):
        return self.id

    def is_connected(self):
        return self.connection != None


class Sensor(Device):
    def update_data(self):
        raise NotImplementedError


class Actuator(Device):
    def evaluate(self):
        raise NotImplementedError
