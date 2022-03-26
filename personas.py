from items import Armor
class Player:
    # strength - defence - speed - stamina
    FIGHTER = [6, 3, 4, 7] 
    PRIEST = [3, 6, 5, 7]
    ELF = [4, 3, 6, 7]
    ORC = [4, 3, 5, 8]

    def __init__(self, name, tipo):
        self.life = 20
        self.name = name
        self.tipo = tipo
        self.level = 1
        self.money = 1
        self.potions = 4
        self.pos = 'r'
        self.weapon = 'no weapon'
        self.armor = Armor('None', 0, 0, 0)
        self.std_life = self.life
        self.type_status()

    def restart(self):
        self.life = (self.std_life + self.level - 1)
        self.std_life = self.life
        self.potions = (self.level - 1) if (self.level > 4) else 4
        self.pos = 'r'
        self.stamina = (self.level * 2) if (self.level * 2 >= 7) else 8

        self.strength += 1
        self.defence += 1
        self.speed += 1

    def type_status(self):
        if self.tipo == 'fighter':
            self.strength, self.defence, self.speed, self.stamina = self.FIGHTER
        elif self.tipo == 'priest':
            self.strength, self.defence, self.speed, self.stamina = self.PRIEST
        elif self.tipo == 'elf':
            self.strength, self.defence, self.speed, self.stamina = self.ELF
        elif self.tipo == 'orc':
            self.strength, self.defence, self.speed, self.stamina = self.ORC

    def set_weapon(self, item):
        self.weapon = item

    def set_armor(self, item):
        self.armor = item

    def get_attack(self, prob):
        self.stamina -= 1
        if self.stamina > 0:
            if prob > 7:
                return self.weapon.damage + self.strength + self.speed
            return self.weapon.damage + self.strength
        return 0

    def get_defence(self, prob):
        if prob > 7:
            self.stamina += 1
            return self.armor.damage + self.defence + self.speed
        else:
            return self.armor.damage + self.defence

    def move(self, move):
        if move == 'r':
            self.pos = 'r'
        elif move == 'l':
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

    def get_movement(self, prob):
        movimento = self.sequence[self.index]
        self.index = (self.index + 1) if (self.index < len(self.sequence) - 1) else 0
        return movimento

    def get_defence(self):
        return self.defence + int(self.stamina / 3)

    def get_attack(self):
        return self.strength + self.speed + int(self.stamina / 2)
    

    def __repr__(self) -> str:
        return f"{self.name},{self.description}"