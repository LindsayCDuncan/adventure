class Character:
    """ Base character class. """
    def __init__(self, name="Generic Character", max_health=50, damage=5):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.damage = damage
        self.alive = True

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health <= 0:
            self.death()

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def attack(self, other):
        if isinstance(other, Character):
            other.take_damage(self.damage)

    def death(self):
        self.alive = False

    def is_alive(self):
        return self.current_health > 0

    def __str__(self):
        description = "Name: {} \n" \
                      "Current Health: {} \n" \
                      "Maximum Health: {} \n" \
                      "Damage: {}".format(self.name, str(self.current_health),
                                          str(self.max_health), str(self.damage))
        return description
