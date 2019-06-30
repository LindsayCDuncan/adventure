from character import Character
from player import Player
from math import floor
from random import randint


class Enemy(Character):
    def __init__(self, name="Bad Guy", other=None):
        Character.__init__(self, name)
        self.level = self.init_level(other)
        self.exp_reward = self.init_exp_reward()
        self.max_health = self.init_health()
        self.current_health = self.max_health
        self.damage = self.init_damage()

    def init_level(self, other):
        if isinstance(other, Player):
            min_level = other.level if other.level > 1 else 1
            max_level = other.level + 2
        else:
            min_level = 1
            max_level = 3

        return randint(min_level, max_level)

    def init_exp_reward(self):
        reward_modifier = 1.7
        return 10 + floor(self.level ** reward_modifier)

    def init_health(self):
        base = 20
        health_modifier = 2
        return base + floor(self.level ** health_modifier)

    def init_damage(self):
        base = 4
        dmg_modifier = 0.9
        return base + floor(self.level ** dmg_modifier)

    def __str__(self):
        description = super().__str__() + "\nLevel: {} \n" \
                                          "Exp reward: {}".format(str(self.level),
                                                                  str(self.exp_reward))
        return description

