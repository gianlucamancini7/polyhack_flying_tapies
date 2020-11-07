class Device:

    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.data = None
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

