from personas import Player, Boss
from items import Shop, Weapon
from random import randint

BOSSES_NAMES = ['Pupu', 'Harold', 'Manny', 'Grudge', 'Garfor', 'Nemus', 'Yaijin', 'Kai', 'Porpheus', 'Villean', 'Frosty']
DEFEATED_BOSSES = []

def set_boss_list():
    boss_list = open('bosses.txt', 'r').read().split('\n')
    LISTONA = []

    for boss in boss_list:
        nome, description = boss.split(',')
        LISTONA.append(Boss(nome, description))

    return LISTONA

# ------------------------------------------------------------

def fight(player, boss):
    print("-------------ON COMBAT----------------")
    print("Remember: 'r' is right, 'l' is left, 'a' is attack, 'd' if defend, 'h' if heal (drink potion)")
    print(f"You enconter {boss}\n")
    lutando = True

    while lutando:
        print(f"\nBoss:{boss.life} <-> {player.name}:{player.life}?{player.stamina}")
        move = input("Do a move: [r,l,a,d,h]: ").lower()
        if move == 'l' or move == 'r': player.move(move)
        elif move == 'a': player.get_attack(randint(0,10))
        elif move == 'd': player.get_defence(randint(0,10))
        elif move == 'h': player.drink_potion()
        else: move == None
        player.stamina  = player.stamina if player.stamina >= 0 else 0

        chefe_move = boss.get_movement(randint(0,10))

        print(f'> {boss} did "{chefe_move}"')

        # If the player moves
        if move != None:
            if move in ['l,','r']:
                if (move == chefe_move) or (chefe_move == 'b'):
                    dano = boss.get_attack() - player.speed
                    player.get_damage(dano - player.get_defence(randint(0,10)))
                    print(f"{boss} gave {dano} of damage")
                    player.stamina -= 1

            elif move == 'd':
                if chefe_move in ['r','l','b']:
                    dano = boss.get_attack()
                    player.get_damage(dano - (player.get_defence(10)))
                    print(f"{boss} gave {dano} of damage")
                    player.stamina -= 1

                elif chefe_move == 'h':
                    boss.life += int(boss.stamina / boss.speed)
                    print(f"{boss} healed")
                player.stamina += 1

            elif move == 'h':
                if (player.pos == chefe_move) or (chefe_move == 'b'):
                    dano = boss.get_attack()
                    player.get_damage(dano - player.get_defence(randint(0,10)))
                    player.stamina -= 1
                    print(f"{boss} gave {dano} of damage")

                elif chefe_move == 'h':
                    boss.life += int(boss.stamina / boss.speed)
                    print(f"{boss} healed")
                player.drink_potion()

            elif move == 'a':
                p_dano = player.get_attack(randint(0,10))
                if (player.pos == chefe_move) or (chefe_move == 'b'):
                    dano = boss.get_attack()
                    player.get_damage(dano - player.get_defence(randint(0,10)))
                    p_dano = p_dano - boss.defence
                    boss.life = boss.life - p_dano if p_dano > 0 else boss.life
                    print(f"{boss} gave {dano} of damage")
                    print(f"{player.name} gave {p_dano} of damage")

                elif chefe_move in ['l','r']:
                    p_dano = p_dano - boss.defence
                    boss.life = boss.life - p_dano if p_dano > 0 else boss.life
                    print(f"{player.name} gave {p_dano} of damage")

                elif chefe_move == 'd':
                    p_dano = p_dano - (boss.defence + boss.stamina)
                    boss.life = (boss.life - p_dano) if p_dano > 0 else boss.life
                    print(f"{player.name} gave {p_dano} of damage")

                elif chefe_move == 'h':
                    p_dano = p_dano - (boss.defence + boss.stamina)
                    boss.life = (boss.life - p_dano) if p_dano > 0 else boss.life
                    boss.life += int(boss.stamina / boss.speed)
                    print(f"{player.name} gave {p_dano} of damage, but {boss} healed")
        # If he/she doesn't move
        else:
            if chefe_move in ['r','l','b']:
                dano = boss.get_attack()
                player.get_damage(dano - player.defence)
                print(f"{boss} gave {dano} of damage")

            elif chefe_move == 'd':
                print(f"{boss} defended")

            elif chefe_move == 'h':
                boss.life += int(boss.stamina / boss.speed)
                print(f"{boss} healed")

        # To garantee non superior life
        if boss.life > boss.std_life:
            boss.life = boss.std_life
        if player.life > 20 * player.level:
            player.life = 20 * player.level

        # If one of them died
        if player.life <= 0:
            print(f"The player {player.name} was defetead by {boss}")

            if randint(0,boss.std_life) < boss.speed:
                print("You gain pity money")
                player.money += 2

            lutando = False
        elif boss.life <= 0:
            print(f"The player {player.name} defetead {boss}")
            DEFEATED_BOSSES.append(boss)
            player.level_up()
            lutando = False
        print()

    player.restart()
    boss.set_status()
    return None

def menu(player, shop, bosses):
    rodando = True
    while rodando:
        if len(DEFEATED_BOSSES) == len(BOSSES_NAMES):
            print(f"{player.name} defeated everone! Congrats")
            rodando = False
            break

        print("----------ON THE MENU---------")
        print("(0 - Leave) (1 - Check profile) - (2 - Shop) (3 - Boss List)")
        esc = input("What would you like to do?: ")
        print()

        if esc not in ['0','1','2','3']:
            print("Wrong choice, buddy!")
        else:
            esc = int(esc)

            if esc == 0:
                rodando = False
            elif esc == 1:
                print(f"{player} # {player.weapon} # ${player.money} # {player.potions} potions")
                print()
            elif esc == 2:
                shop.introduce(player)
                print()
            elif esc == 3:
                if isinstance(player.weapon, Weapon) == False:
                    print("You need a weapon, buddy")
                else:
                    print("\nPlease, choose one of the bosses below: ")
                    for b in range(len(bosses)): print(f"[{b}] {bosses[b]} ({bosses[b] in DEFEATED_BOSSES})")
                    chefao = input("Your choice (by name): ")

                    if chefao not in BOSSES_NAMES:
                        print("This boss doesn't exist (or you wrote is name not precisely correct)\n")
                    else:
                        chefao = bosses[BOSSES_NAMES.index(chefao)]
                        if chefao in DEFEATED_BOSSES:
                            print("Oh man, you already defeated that one.\n")
                        else:
                            fight(player, chefao)

if __name__ == '__main__':
    print("""
        Welcome to the mini-game of Boss Fighting.
        In this game you'll fight bosses (as the title sugests).
        Good luck.
    """)
    nome = input("But first, what is your name: ")
    print("\nCLASSES: (0) Fighter - (1) Priest - (2) Elf - (3) Orc")
    clase = input("Wich class you desire to be? (Choose by name): ").lower()
    print()
    JOGADOR = Player(nome, clase)

    SHOP = Shop()
    BOSSES = set_boss_list()

    menu(JOGADOR, SHOP, BOSSES)

    print("Thank you for playing :)")