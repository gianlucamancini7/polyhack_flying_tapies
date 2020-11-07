class Device:

    def __init__(self, id_, ty):
        self.id = id_
        self.ty = ty
        self.data = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
