
class Weapon:
    def __init__(self, name, level, damage, cost):
        self.name = name
        self.level = level
        self.damage = damage
        self.cost = cost

    def __repr__(self) -> str:
        return f"Weapon({self.name}:lv{self.level}:{self.damage}dm:${self.cost})"

class Shop:
    W_NAMES = [
        'Dagger', 'Medium Sword', 'Long Sword', 'Heavy Axe', 'Katana', 'Bow&Arrows', 'Staff', 'Long Spear', 'Large Blade'
    ]
    W_STATS = [
        [1,1,1], [2,2,6], [3,3,10], [5,6,15], [6,7,18], [7,8,26], [8,10,32], [9,11,43], [10,12,56]
    ] # Stats = [level, damage, cost]

    def __init__(self):
        self.weapons = []
        self.set_default()

    def set_default(self):
        for name, stats in zip(self.W_NAMES, self.W_STATS):
            self.weapons.append(
                Weapon(name, stats[0], stats[1], stats[2])
            )

    def introduce(self, player):
        print(f"Oh, hello {player.name}. Would you like to buy some of my stuff?")
        on_shop = True

        while on_shop:
            print("------ON THE SHOP-------")
            print("(0) Buy Weapon - (1) Buy Potion - (2) Updgrade - (3) Leave")
            esc = int(input(">> Your choice (by index): "))

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
                potions = int(input("\nHow many do you want?: "))
                price = potions * 2
                if price > player.money:
                    print(f"I see you don't have the money to buy {potions} potions.\n")
                else:
                    player.potions += 1
                    print("Here it is!\n")

            elif esc == 2:
                calc = int((player.level * 10) / 2)
                if calc > player.money:
                    print(f"Sorry, you need ${calc} to upgrade from level {player.level}")
                else:
                    print("Here you go! Upgrade")
                    player.level_up()

        print("Thanks for coming :)\n")