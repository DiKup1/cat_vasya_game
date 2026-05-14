from abc import ABC, abstractmethod


class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        pass

class Fireball(Spell):
    def __init__(self):
        super().__init__(name="Fireball", damage=35, mana_cost=15)

    def cast(self):
        return self.damage

class IceLance(Spell):
    def __init__(self):
        super().__init__(name="IceLance", damage=25, mana_cost=10)

    def cast(self):
        return self.damage

class LightningBolt(Spell):
    def __init__(self):
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self):
        return self.damage