import json


class Location:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = ""
        self.has_enemy = False
        self.has_npc = False
        self.has_investigate = False

    def __str__(self):
        return "{}".format(self.name)


class LocationJSONEncoder(json.JSONEncoder):
    def default(self, o):
        """ Encode location objects into json format. Return as dictionary. """
        d = dict()
        d["id"] = o.id
        d["name"] = o.name
        d["description"] = o.description
        d["enemy"] = o.has_enemy
        d["npc"] = o.has_npc
        d["investigate"] = o.has_investigate
        d["north"] = o.north
        d["east"] = o.east
        d["south"] = o.south
        d["west"] = o.west
        return d






