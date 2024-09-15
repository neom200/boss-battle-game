# from genericpath import isdir
from personas import Player, Boss
from items import Armor, Shop, Weapon
from random import randint
from definitions import BOSSES
import json

BOSSES_NAMES = ['Pupu', 'Harold', 'Manny', 'Grudge', 'Garfor', 'Nemus', 'Yaijin', 'Kai', 'Porpheus', 'Villean', 'Frosty', 'Shamack']
DEFEATED_BOSSES = []

def set_boss_list():
    boss_list = BOSSES.split('\n')
    LISTONA = []
    
    for boss in boss_list:
        nome, description = boss.split(',')
        LISTONA.append(Boss(nome, description))

    return LISTONA

"""def set_boss_list():
    boss_list = open('bosses.txt', 'r').read().split('\n')
    LISTONA = []

    for boss in boss_list:
        nome, description = boss.split(',')
        LISTONA.append(Boss(nome, description))

    return LISTONA"""

# ------------------------------------------------------------

def fight(player, boss):
    print("-------------ON COMBAT----------------")
    print("Remember: 'r' is right, 'l' is left, 'a' is attack, 'd' if defend, 'h' if heal (drink potion)")
    print("Also remember what the data means: Boss <-> You[Pos]:Life?Stamina@Potions")
    print(f"You enconter {boss}\n")
    lutando = True

    while lutando:
        print(f"\nBoss:{boss.life} <-> {player.name}[{player.pos.upper()}]:{player.life}?{player.stamina}@{player.potions}")
        move = input("Do a move: [r,l,a,d,h]: ").lower()

        if move == 'l' or move == 'r': 
            player.move(move)
        player.stamina  = player.stamina if player.stamina >= 0 else 0

        chefe_move = boss.get_movement()
        print(f'> {boss} did "{chefe_move}"')

        # If the player moves
        if move != None:

            if move in ['l,','r']:
                if (player.pos == chefe_move):
                    dano = boss.get_attack() - player.get_defence(randint(0,10))

                    if randint(0, player.speed) > randint(0, boss.speed):
                        dano -= player.get_defence(randint(0,10))
                    player.get_damage(dano)
                    print(f"{boss} gave {dano} of damage")
                
                player.stamina += 1

            elif move == 'd':
                if (player.pos == chefe_move):
                    dano = boss.get_attack() - player.get_defence(randint(0,10))
                    player.get_damage(dano)
                    print(f"{boss} gave {dano} of damage")
                    player.stamina += 1

            elif move == 'h':
                if (player.pos == chefe_move):
                    dano = boss.get_attack() - player.get_defence(randint(0,10))
                    player.get_damage(dano)
                    player.stamina += 1
                    print(f"{boss} gave {dano} of damage")

                player.drink_potion()

            elif move == 'a':
                p_dano = player.get_attack(randint(0,10)) + player.do_combo(move)
                if (player.pos == chefe_move):
                    dano = boss.get_attack() - player.get_defence(randint(0,10)) - player.do_combo(move)
                    player.get_damage(dano if dano > 0 else 0)
                    p_dano = p_dano - boss.get_defence()
                    boss.life = boss.life - p_dano if p_dano > 0 else boss.life
                    print(f"{boss} gave {dano} of damage")
                    print(f"{player.name} gave {p_dano} of damage")

                elif chefe_move in ['l','r']:
                    p_dano = p_dano - boss.get_defence() - player.do_combo(move)
                    boss.life = boss.life - p_dano if p_dano > 0 else boss.life
                    print(f"{player.name} gave {p_dano} of damage")

                elif chefe_move == 'd':
                    p_dano = p_dano - (boss.get_defence() + boss.stamina) - player.do_combo(move)
                    boss.life = (boss.life - p_dano) if p_dano > 0 else boss.life
                    print(f"{player.name} gave {p_dano} of damage")

        # If he/she doesn't move
        else:
            if chefe_move in ['r','l','b']:
                dano = boss.get_attack()
                player.get_damage(dano - player.defence)
                print(f"{boss} gave {dano} of damage")

            elif chefe_move == 'd':
                print(f"{boss} defended")

        # To garantee non superior life
        if boss.life > boss.std_life:
            boss.life = boss.std_life
        if player.life > 20 * player.level:
            player.life = 20 * player.level

        # If one of them died
        if player.life <= 0:
            print(f"The player {player.name} was defetead by {boss}")

            if randint(0, boss.strength) > boss.stamina:
                print("You gain pity money")
                player.money += 1

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

def save_menu(player):
    from os import mkdir
    from os.path import isdir
    from json import dump

    if isdir('./saves/') == False:
        mkdir('./saves/', mode=0o666)
    
    player_infos = {}
    # Saving player's infos in a dict
    player_infos['NAME'] = player.name
    player_infos['TIPO'] = player.tipo
    player_infos['STATUS'] = {
        'std_life': player.std_life,
        'strength': player.strength,
        'defence': player.defence,
        'speed': player.speed,
        'stamina': player.stamina
    }
    player_infos['POTIONS'] = player.potions
    player_infos['MONEY'] = player.money
    player_infos['WEAPON'] = {
        'name': player.weapon.name,
        'level': player.weapon.level,
        'damage': player.weapon.damage,
        'cost': player.weapon.cost
    }
    player_infos['ARMOR'] = {
        'name': player.armor.name,
        'level': player.armor.level,
        'damage': player.armor.damage,
        'cost': player.armor.cost
    }
    player_infos['DEFEATEDS'] = [boss.name for boss in DEFEATED_BOSSES]

    save_path = f'saves/{player.name}_info.json'
    try:
        with open(save_path, "w") as arquiv:
            json.dump(player_infos, arquiv, indent=4)
    except Exception as e:
        raise Exception(f"Não foi possivel salvar o status atual. Motivo: {str(e)}")

    return save_path

    print(f"{player.name}'s data saved successfully.\n")

def menu(player, shop, bosses):
    rodando = True

    while rodando:
        if len(DEFEATED_BOSSES) == len(BOSSES_NAMES):
            print(f"{player.name} defeated everone! Congraulations, noble hero of the kingdown, now go and marry the princess, and together you both will live a happy life with the fame and glory the gods have given you!")
            rodando = False
            break

        print("----------ON THE MENU---------")
        print("(0 - Leave) (1 - Check profile) (2 - Shop) (3 - Boss List) (4 - Save)")
        esc = input("What would you like to do?: ")
        print()

        if esc not in ['0','1','2','3', '4']:
            print("Wrong choice, buddy!")
        else:
            esc = int(esc)

            if esc == 0:
                rodando = False
            elif esc == 1:
                print(f"{player}\n# {player.weapon} # {player.armor} # ${player.money} # {player.potions} potions")
                print()
            elif esc == 2:
                shop.introduce(player)
                print()
            elif esc == 3:
                if isinstance(player.weapon, Weapon) == False:
                    print("You need a weapon, buddy")
                else:
                    print("\nPlease, choose one of the bosses below: ")
                    for b in range(len(bosses)): print(f"[{b+1}] {bosses[b]} ({bosses[b] in DEFEATED_BOSSES})")
                    chefao = input("Your choice (by name): ")

                    if chefao not in BOSSES_NAMES:
                        print("This boss doesn't exist (or you wrote is name incorrectly)\n")
                    else:
                        chefao = bosses[BOSSES_NAMES.index(chefao)]
                        if chefao in DEFEATED_BOSSES:
                            print("Oh man, you already defeated that one.\n")
                        else:
                            fight(player, chefao)
            elif esc == 4:
                file = save_menu(player)
                print("#> Dados do jogador salvos em:", file)
                #print("The save option is under construction, im sorry :(\n")

def fix_class_choice(choice):
    if choice == '0' or choice == 'fighter' or choice == 'Fighter':
        return 'fighter'
    if choice == '1' or choice == 'priest' or choice == 'Priest':
        return 'priest'
    if choice == '2' or choice == 'elf' or choice == 'Elf':
        return 'elf'
    if choice == '3' or choice == 'orc' or choice == 'Orc':
        return 'orc'
    return 'fighter'

if __name__ == '__main__':
    from os.path import exists
    from json import load

    print("""
    In the far lands of Habnamia, after the death of King Absalom III, head of the House of Hellosberg, the kingdown saw the arise of 12 dangerous and powerful monstrosities, and soon all land was quivering in fear.
    Now you, fellow adventurer, has come from nothing but a humble family to complete the task given to all men by the Queen Rasphelia, wich is to defeat all 12 monsters, with the garantuee of being rewarded not only with prestigious, fame and glory, but also the right to marry the beautiful Princess Myrian.
    """)

    nome = input("But first, what is your name: ")

    if exists(f'./saves/{nome}_info.json'):
        print("A player file with this name already exists.")
        esc = input("Wanna use it? (Y/N): ").lower()
        if esc == 'y':
            with open(f'./saves/{nome}_info.json', 'r') as player_info:
                dados = load(player_info)
                tipo = dados['TIPO']
                status = dados['STATUS']
                potions = dados['POTIONS']
                money = dados['MONEY']
                weapon = dados['WEAPON']
                armor = dados['ARMOR']
                DEFEATED_BOSSES_NAMES = dados['DEFEATEDS']

                SHOP = Shop()
                BOSSES = set_boss_list()

                for b in BOSSES:
                    if b.name in DEFEATED_BOSSES_NAMES:
                        DEFEATED_BOSSES.append(b)

                JOGADOR = Player(nome, tipo)
                JOGADOR.money = money
                JOGADOR.potions = potions
                JOGADOR.weapon = Weapon(weapon['name'], weapon['level'], weapon['damage'], weapon['cost'])
                JOGADOR.armor = Armor(armor['name'], armor['level'], armor['damage'], armor['cost'])
                JOGADOR.strength = status['strength']
                JOGADOR.defence = status['defence']
                JOGADOR.speed = status['speed']
                JOGADOR.stamina = status['stamina']
                JOGADOR.std_life = status['std_life']

                print()

        elif esc == 'n':
            print("\nCLASSES: (0) Fighter - (1) Priest - (2) Elf - (3) Orc")
            clase = input("Wich class you desire to be? (Choose by name): ").lower()
            clase = fix_class_choice(clase)

            print()
            JOGADOR = Player(nome, clase)
            #print(f"{JOGADOR.tipo}")
            SHOP = Shop()
            BOSSES = set_boss_list()
        else:
            print("You didn't answer correctly. BYE!")

    else:
        print("\nCLASSES: (0) Fighter - (1) Priest - (2) Elf - (3) Orc")
        clase = input("Wich class you desire to be? (Choose by name or number): ").lower()
        clase = fix_class_choice(clase)

        print()
        JOGADOR = Player(nome, clase)
        SHOP = Shop()
        BOSSES = set_boss_list()

    menu(JOGADOR, SHOP, BOSSES)

    print("Thank you for playing:)")
