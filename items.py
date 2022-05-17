
class Weapon:
    def __init__(self, name, level, damage, cost):
        self.name = name
        self.level = level
        self.damage = damage
        self.cost = cost

    def __repr__(self) -> str:
        return f"Weapon({self.name}:lv{self.level}:{self.damage}dm:${self.cost})"

class Armor:
    def __init__(self, name, level, damage, cost):
        self.name = name
        self.level = level
        self.damage = damage
        self.cost = cost

    def __repr__(self) -> str:
        return f"Armor({self.name}:lv{self.level}:{self.damage}dm:${self.cost})"

class Shop:
    W_NAMES = [
        'Dagger', 'Medium Sword', 'Long Sword', 'Heavy Axe', 'Katana', 'Bow&Arrows', 'Staff', 'Long Spear', 'Large Blade'
    ]
    W_STATS = [
        [1,1,1], [2,3,6], [3,4,9], [5,7,14], [6,8,16], [7,9,23], [8,12,29], [9,13,35], [10,15,40]
    ] # Stats = [level, damage, cost]

    A_NAMES = [
        'Bandit Armor', 'Leather Armor', 'Copper Armor', 'Silver Armor', 'Golden Armor', 'Iron Armor', 'Steel Armor', 'Obsidian Armor'
    ]
    A_STATS = [
        [2,3,5], [3,4,9], [5,7,14], [6,8,16], [7,9,23], [8,11,29], [9,12,35], [10,15,40]
    ] # Stats = [level, protection, cost]

    def __init__(self):
        self.weapons = []
        self.armors = []
        self.set_default()

    def set_default(self):
        for name, stats in zip(self.W_NAMES, self.W_STATS):
            self.weapons.append(
                Weapon(name, stats[0], stats[1], stats[2])
            )
        for name, stats in zip(self.A_NAMES, self.A_STATS):
            self.armors.append(
                Armor(name, stats[0], stats[1], stats[2])
            )

    def introduce(self, player):
        print(f"Oh, hello {player.name}. Would you like to buy some of my stuff?")
        on_shop = True

        while on_shop:
            print("------ON THE SHOP-------")
            print("(0) Buy Weapon - (1) Buy Armor - (2) Buy Potion - (3) Leave")
            esc = input(">> Your choice (by index): ")

            if esc in ['0','1','2','3']:
                esc = int(esc)
            else:
                print("This option doesn't exist my friend!")

            print()
            if esc == 3:
                on_shop = False
            elif esc == 0:
                for w in range(len(self.weapons)): 
                    print(f"({w}):{self.weapons[w]}")
                arma = int(input("Please, choose by index: "))
                
                if arma < 0 or arma > len(self.weapons)-1:
                    print("This index is incorret!\n")
                else:
                    arma = self.weapons[arma]
                    if player.money < arma.cost:
                        print("Oh man, you can't buy it, sorry :(\n")
                    else:
                        player.money -= arma.cost
                        player.set_weapon(arma)
                        print("Here it is!\n")

            elif esc == 1:
                for w in range(len(self.armors)): 
                    print(f"({w}):{self.armors[w]}")
                arma = int(input("Please, choose by index: "))
                
                if arma < 0 or arma > len(self.armors)-1:
                    print("This index is incorret!\n")
                else:
                    arma = self.armors[arma]
                    if player.money < arma.cost:
                        print("Oh man, you can't buy it, sorry :(\n")
                    else:
                        player.money -= arma.cost
                        player.set_armor(arma)
                        print("Here it is!\n")


            elif esc == 2:
                potions = int(input("\nHow many do you want?: "))
                price = potions * 2
                if price > player.money:
                    print(f"I see you don't have the money to buy {potions} potions.\n")
                else:
                    player.potions += 1
                    print("Here it is!\n")

        print("Thanks for coming :)\n")