from items import Armor
from random import randint
class Player:
    # strength - defence - speed - stamina
    FIGHTER = [7, 4, 5, 8] 
    PRIEST = [4, 7, 6, 8]
    ELF = [5, 4, 7, 8]
    ORC = [5, 4, 6, 9]

    def __init__(self, name, tipo):
        self.life = 20
        self.name = name
        self.tipo = tipo
        self.level = 1
        self.money = 1
        self.potions = 5
        self.pos = 'r'
        self.weapon = 'no weapon'
        self.armor = Armor('None', 0, 0, 0)
        self.std_life = self.life
        self.type_status()
        self.movements = []

    def restart(self):
        self.life = (self.std_life + self.level - 1)
        self.std_life = self.life
        self.potions = (self.level - 1) if (self.level > 4) else 4
        self.pos = 'r'
        self.stamina = (self.level * 2) if (self.level * 2 >= 7) else 8
        self.movements = []
        # self.strength += 1
        # self.defence += 1
        # self.speed += 1

    def type_status(self):
        if self.tipo == 'fighter':
            self.strength, self.defence, self.speed, self.stamina = self.FIGHTER
        elif self.tipo == 'priest':
            self.strength, self.defence, self.speed, self.stamina = self.PRIEST
        elif self.tipo == 'elf':
            self.strength, self.defence, self.speed, self.stamina = self.ELF
        elif self.tipo == 'orc':
            self.strength, self.defence, self.speed, self.stamina = self.ORC

    def do_combo(self, move):
        combo = self.movements[-3:]
        if combo == ['a','a','a'] and move == 'a':
            return int(self.strength / 2)
        elif combo == ['d','d','d'] and move == 'd':
            return self.defence * 2
        elif combo == ['r','l','r'] and move == 'l':
            return int(self.defence / 2)
        elif combo == ['l','r','l'] and move == 'r':
            return int(self.defence / 2)
        elif combo == ['d','a','d'] and move == 'a':
            return int(self.strength / 3)

        return 0

    def set_weapon(self, item):
        self.weapon = item

    def set_armor(self, item):
        self.armor = item

    def get_attack(self, prob):
        self.movements.append('a')
        self.stamina -= 1
        if self.stamina > 0:
            if prob > 6:
                return self.weapon.damage + self.strength + self.speed
            return self.weapon.damage + self.strength
        return 0

    def get_defence(self, prob):
        self.movements.append('d')
        self.stamina += 1
        if prob > 6:
            return self.armor.damage + self.defence + self.speed
        else:
            return self.armor.damage + self.defence

    def move(self, move):
        if move == 'r':
            self.movements.append('r')
            self.pos = 'r'
        elif move == 'l':
            self.movements.append('l')
            self.pos = 'l'

    def drink_potion(self):
        if self.potions > 0:
            calc = self.level * 2
            self.life = (self.life + calc) if (self.life + calc < self.std_life) else self.std_life
            self.potions -= 1
        else:
            print("\tNo potions left\n")
        self.stamina += 1

    def get_damage(self, dano):
        if dano > 0:
            self.life = (self.life - dano) if (dano < self.life) else 0

    def level_up(self):
        self.level += 1
        self.money += self.level
        self.std_life += self.level + 1
    
    def __repr__(self) -> str:
        return f"[{self.name}:{self.tipo}:lv.{self.level}]->[{self.strength},{self.defence},{self.speed},{self.stamina}]"

# -----------------------------------------------------------------------
class Boss:
    STATUS = open('boss_status.txt', 'r').read().split('\n')
    STYLES = open('boss_styles.txt', 'r').read().split('\n')
    BOSSES_NAMES = ['Pupu', 'Harold', 'Manny', 'Grudge', 'Garfor', 'Nemus', 'Yaijin', 'Kai', 'Porpheus', 'Villean', 'Frosty', 'Shamack']

    def __init__(self, name, description, ):
        self.name = name
        self.description = description
        self.set_status()

    def set_status(self):
        seus_status = self.STATUS[self.BOSSES_NAMES.index(self.name) + 1].split(',')
        self.sequence = self.STYLES[self.BOSSES_NAMES.index(self.name) + 1].split(',')
        self.index = 0

        self.life = int(seus_status[0])
        self.std_life = self.life
        self.strength = int(seus_status[1])
        self.defence = int(seus_status[2])
        self.speed = int(seus_status[3])
        self.stamina = int(seus_status[4])
        self.std_stamina = self.stamina

    def get_movement(self):
        if self.stamina > 0:
            movimento = self.sequence[self.index]
            self.index = (self.index + 1) if (self.index < len(self.sequence) - 1) else 0
            return movimento
        self.stamina += 1
        return None

    def get_defence(self):
        self.stamina += 1
        return self.defence + randint(0, self.speed)

    def get_attack(self):
        if self.stamina > 0:
            self.stamina -= 1
            return self.strength + randint(0, self.speed)
    

    def __repr__(self) -> str:
        return f"{self.name},{self.description}"