class Device:

    def __init__(self, id, ty):
        self.id = id
        self.type = ty
        self.data = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
