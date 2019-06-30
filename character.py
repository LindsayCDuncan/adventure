class Character:
    def __init__(self, name="Generic Character", max_health=50, damage=5):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.damage = damage

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
            print(f"{self.name} attacks {other.name} for {self.damage} damage")
            other.take_damage(self.damage)

    def death(self):
        print(f"{self.name} has died!")

    def is_alive(self):
        return self.current_health > 0

    def __str__(self):
        description = "Name: {} \n" \
                      "Current Health: {} \n" \
                      "Maximum Health: {} \n" \
                      "Damage: {}".format(self.name, str(self.current_health),
                                          str(self.max_health), str(self.damage))
        return description
