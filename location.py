class Location:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = ""
        self.contents = []

    def __str__(self):
        return "{}".format(self.name)


