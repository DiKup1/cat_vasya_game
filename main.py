from character import Character
from monster import Monster
from spell import Fireball

warrior = Character(20, 15, 10, 8, 6, 10, 'warrior')
print(f"Воин: HP={warrior.max_health}, Урон={warrior.damage}")

goblin = Monster(10, 13, 10, 5, 3, 2)
print(f"Гоблин: HP={goblin.max_health}, Урон={goblin.damage}")

mage = Character(7, 5, 12, 13, 18, 7, 'mage')
mage.add_spell(Fireball())
damage = mage.cast_spell(0)
print(f"Маг использовал Fireball и нанёс {damage} урона")