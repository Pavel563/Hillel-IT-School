# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.


class Unit:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 1
        self.dexterity = 1
        self.intelligence = 1
        self.special_skill = ""

    def __repr__(self):
        return f"Name: {self.name}; " \
               f"Clan: {self.clan}; " \
               f"Speacial skill: {self.special_skill}; " \
               f"Health: {self.health}, " \
               f"Power: {self.power}, " \
               f"Dexterity: {self.dexterity}, " \
               f"Intelligence: {self.intelligence}"

    def healing(self):
        self.health += 10
        if self.health >= 100:
            self.health = 100

    def increase_skill(self):
        if self.clan == "Mage":
            self.intelligence += 1
            if self.intelligence >= 10:
                self.intelligence = 10
        if self.clan == "Archer":
            self.dexterity += 1
            if self.dexterity >= 10:
                self.dexterity = 10
        if self.clan == "Knight":
            self.power += 1
            if self.power >= 10:
                self.power = 10


class Mage(Unit):

    def __init__(self, name, clan, magic_type):
        super().__init__(name, clan)
        self.special_skill = magic_type


class Archer(Unit):

    def __init__(self, name, clan, bow_type):
        super().__init__(name, clan)
        self.special_skill = bow_type


class Knight(Unit):

    def __init__(self, name, clan, weapon_type):
        super().__init__(name, clan)
        self.special_skill = weapon_type


mage = Mage("Aang", "Mage", "Wind")
print(mage)
mage.increase_skill()
mage.healing()
print(mage)
archer = Archer("Legolass", "Archer", "Bow")
print(archer)
archer.increase_skill()
print(archer)
knight = Knight("Arthur", "Knight", "Sword")
print(knight)
knight.increase_skill()
print(knight)
