from unit import Unit


class Character(Unit):
    VALID_CLASSES = ('warrior', 'mage', 'hunter')

    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class):
        if character_class not in self.VALID_CLASSES:
            raise ValueError(f"Неверный класс персонажа: {character_class}. Допустимые значения: {self.VALID_CLASSES}")
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        return int(self.constitution * 15 + self.strength / 3)

    def calculate_damage(self):
        if self.character_class == 'warrior':
            return int(self.strength * 2 + self.constitution / 4)
        elif self.character_class == 'mage':
            return int(self.intelligence * 3 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 2 + self.strength / 3)
        return 0

    def calculate_defense(self):
        if self.character_class == 'warrior':
            return int(self.constitution * 2 + self.strength / 4)
        elif self.character_class == 'mage':
            return int(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.6 + self.constitution / 5)
        return 0

    def calculate_max_mana(self):
        if self.character_class == 'warrior':
            return int(self.intelligence + self.strength // 2)
        elif self.character_class == 'mage':
            return int(self.intelligence * 3 + self.wisdom)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.5 + self.wisdom // 2)
        return 0