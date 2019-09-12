from character import Character
from math import floor
import json


class Player(Character):
    def __init__(self, location, name="Hero"):
        Character.__init__(self, name)
        self.level = 1
        self.max_exp = 25
        self.current_exp = 0
        self.current_loc = location

    def level_up(self):
        """ Increase stats when level up. """
        remaining_amount = self.current_exp - self.max_exp
        self.level += 1
        self.current_exp = remaining_amount
        self.increase_max_exp()
        self.increase_max_health()
        self.increase_damage()
        self.reset_current_health()

    def gain_exp(self, amount):
        self.current_exp += amount

    def ready_to_level(self):
        """ Return whether ready to level up. """
        if self.current_exp >= self.max_exp:
            return True
        return False

    def increase_max_exp(self):
        exp_modifier = 1.5
        self.max_exp = floor(self.max_exp * exp_modifier)

    def increase_max_health(self):
        health_flat_modifier = 10
        self.max_health += health_flat_modifier

    def increase_damage(self):
        damage_modifier = 1.1
        base = 5
        self.damage = floor(base + (self.level ** damage_modifier))

    def reset_current_health(self):
        self.current_health = self.max_health

    def change_location(self, new_loc):
        self.current_loc = new_loc

    def __str__(self):
        description = super().__str__() + "\nLevel: {} \n" \
                                          "Experience: {} / {} \n" \
                                          "Current location: {}".format(str(self.level),
                                                                        str(self.current_exp),
                                                                        str(self.max_exp),
                                                                        self.current_loc)
        return description


class PlayerJSONEncoder(json.JSONEncoder):
    """ Encode player object into JSON format. Return as dictionary. """
    def default(self, o):
        d = dict()
        d["name"] = o.name
        d["max_health"] = o.max_health
        d["current_health"] = o.current_health
        d["damage"] = o.damage
        d["alive"] = o.alive
        d["level"] = o.level
        d["max_exp"] = o.max_exp
        d["current_exp"] = o.current_exp
        return d
