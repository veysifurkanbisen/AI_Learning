import random


def game():
    hero_1 = ""
    hero_2 = ""

    while True:
        hero_1 += input("----- First Hero -----\nPlease type your hero's name: ")
        if hero_1.isspace() or hero_1 == "":
            print( "Your name field cannot be empty!")
            continue
        while True:
            hero_2 += input("----- Second Hero -----\nPlease type your hero's name: ")
            if hero_1 == hero_2:
                print(hero_1, "is taken, please choose another name!")
                continue
            elif hero_2.isspace() or hero_2 == "":
                print( "Your name field cannot be empty!")
                continue
            break
        break

    start(hero_1, hero_2)


def start(hero_1, hero_2):
    hp_first_player = 100
    hp_second_player = 100
    winner = ""

    first_player = choose_start(hero_1, hero_2)
    second_player = ""

    if first_player == hero_1:
        second_player += hero_2
    if first_player == hero_2:
        second_player += hero_1

    print("\nCoin toss result:", first_player, "starts first!\n")

    firstHP = str(f"HP[{hp_first_player}]:" + (int(hp_first_player / 2)) * '|')
    secondHP = str(f"HP[{hp_second_player}]:" + (int(hp_second_player / 2)) * '|')
    print_hero(firstHP, secondHP, first_player, second_player)

    while hp_first_player and hp_second_player > 0:

        hp_second_player -= attack(first_player)
        firstHP = str(f"HP[{hp_first_player}]:" + (int(hp_first_player / 2)) * '|')
        secondHP = str(f"HP[{hp_second_player}]:" + (int(hp_second_player / 2)) * '|')
        print_hero(firstHP, secondHP, first_player, second_player)
        if hp_second_player <= 0:
            winner += first_player
            finish(hero_1, hero_2, winner)

        hp_first_player -= attack(second_player)
        firstHP = str(f"HP[{hp_first_player}]:" + (int(hp_first_player / 2)) * '|')
        secondHP = str(f"HP[{hp_second_player}]:" + (int(hp_second_player / 2)) * '|')
        print_hero(firstHP, secondHP, first_player, second_player)
        if hp_first_player <= 0:
            winner += second_player
            finish(hero_1, hero_2, winner)


def print_hero(hp1, hp2, first_name, second_name, size=70, space=0):
    while first_name or second_name:
        print(first_name[:size].ljust(size) + " " * space + second_name[:size])
        first_name = first_name[size:]
        second_name = second_name[size:]

    while hp1 or hp2:
        print(hp1[:size].ljust(size) + " " * space + hp2[:size])
        hp1 = hp1[size:]
        hp2 = hp2[size:]


def choose_start(*args):
    return random.choice(args)


def is_taken(hero_1, hero_2):
    return hero_1 == hero_2


def attack(attacker):
    print(f"\n----- {attacker} Attacks!! -----")
    while True:
        power = int(input("Choose your attack magnitude between 1 and 50: "))
        if power > 50:
            print("The attack magnitude must be between 1 and 50.")
            continue

        if hit(power):
            print(f"{attacker} hits {power} damage!")
            return power

        print(f"Ooopsy {attacker} missed the attack!")
        return 0


def hit(power):
    prob = []
    for i in range(100):
        if power * 2 < i:
            prob.append(power)
        else:
            prob.append(i)
    if random.choice(prob) == power:
        return True
    else:
        return False


def finish(hero1, hero2, winner):
    win = f" {winner} wins!! "
    print("\n" + 70 * "*" + "\n" + str(int((70 - len(win))/2) * "*") + win + str(int((70 - len(win))/2) * "*") + "\n" + 70 * "*" + "\n")

    while True:
        ask = input("Do you want to play another round (Yes or No)?: ")
        if ask == "yes" or ask == "Yes" or ask == "YES":
            start(hero1, hero2)
        elif ask == "no" or ask == "No" or ask == "NO":
            print("Thanks for playing! See you again!")
            exit()
        else:
            continue
        break


game()
