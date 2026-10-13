from random import randint
import random


class Hero:
    def __init__(self, bonus_hp, bonus_atk, hero_type="", true_name="", hero=None):
        self.__true_name = true_name
        self.hero_type = hero_type
        self.bonus_hp = bonus_hp
        self.bonus_atk = bonus_atk
        self.hero = hero

    def get_truename(self):
        return self.__true_name


class Master_Swordsmen(Hero):
    def __init__(self, bonus_hp=10, bonus_atk=10, hero_type="Master_Swordsmen", true_name="Athena"):

        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)

    def title(self):
        print(self.hero_type, "Tactition")


class Highclass_Tanker(Hero):
    def __init__(self, bonus_hp=40, bonus_atk=5, hero_type="Highclass_Tanker", true_name="Hephaestus"):

        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)

    def title(self):
        print(self.hero_type, "Blacksmith")


class Spirit_Archer(Hero):
    def __init__(self, bonus_hp=0, bonus_atk=15, hero_type="Spirit_Archer", true_name="Artemis"):

        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)

    def title(self):
        print(self.hero_type, "Hunter")


class Elemental_Brawler(Hero):
    def __init__(self, bonus_hp=20, bonus_atk=10, hero_type="Elemental_Brawler", true_name="Ares"):

        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)

    def title(self):
        print(self.hero_type, "Berserker")


class Normal_Guy(Hero):
    def __init__(self, bonus_hp=0, bonus_atk=0, hero_type="Normal_Guy", true_name="One above all"):

        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)
        self.One_Above_All()

    def One_Above_All(self, activation_chance=0.1, passive_dmg=200):
        self.activation_chance = activation_chance
        self.passive_dmg = passive_dmg


class Player:
    def __init__(self, name="", type=Hero):
        self.type = type
        self.name = name
        self.base_hp = 100
        self.base_atk = 10


class Monster:
    def __init__(self, hp=200, dmg=5, name=""):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.dmg = dmg

    def reset(self):
        self.hp = self.max_hp


class Goblin(Monster):
    def __init__(self, hp=200, dmg=5, name="Goblin"):

        super().__init__(hp, dmg, name)


master_swordsmen = Master_Swordsmen()
highclass_tanker = Highclass_Tanker()
spirit_archer = Spirit_Archer()
elemental_brawler = Elemental_Brawler()
normal_guy = Normal_Guy()

goblin = Goblin()


heros = [master_swordsmen, highclass_tanker, spirit_archer, elemental_brawler]

player = None


def game():
    start_game = input(
        "Do you wanna start a new adventure? (y/n): ").lower()

    while True:
        if start_game not in ("yes", "y"):
            break

        player_name = input("NOW CHOOSE YOUR HEROS NAME!!!: ")
        player = Player(player_name)

        print(f"WELCOME {player.name} TO RPG WORLD!!!\n")

        print("CHOOSE YOUR HERO\n")

        print(f"Hero type: {master_swordsmen.hero_type}")
        print(f"Hero true name: {master_swordsmen.get_truename()}\n")

        print(f"Hero type: {highclass_tanker.hero_type}")
        print(f"Hero true name: {highclass_tanker.get_truename()}\n")

        print(f"Hero type: {spirit_archer.hero_type}")
        print(f"Hero true name: {spirit_archer.get_truename()}\n")

        print(f"Hero type: {elemental_brawler.hero_type}")
        print(f"Hero true name: {elemental_brawler.get_truename()}\n")

        choose_hero = input("Choose 1, 2, 3 or 4: ")

        if choose_hero != "none":

            if choose_hero == "1":
                player.type = master_swordsmen

            elif choose_hero == "2":
                player.type = highclass_tanker

            elif choose_hero == "3":
                player.type = spirit_archer

            elif choose_hero == "4":
                player.type = elemental_brawler

        elif choose_hero == "none":
            player.type = normal_guy

        if player.type != None:
            print(f"Your choosen Hero class is {player.type.hero_type} \n")

        while True:
            adventure = input(
                "Are you ready to begin your journey? (y/n): ").lower()

            if adventure not in ("yes", "y"):
                break

            elif adventure in ("yes", "y"):
                while True:

                    print("1. Adventure")
                    print("2. Inventory")
                    print("3. Shop")
                    print("4. Exit Game")

                    choice = input("What do you wanna do?: ").lower()

                    if choice in ("1", "adventure"):
                        goblin = Goblin()
                        print(f"You stumbled upon a {goblin.name}")
                        while True:
                            print(f"It has {goblin.hp} Hp")

                            action = input(
                                "What do you do (attack, run, heal)?: ").lower()
                            if action in ("attack", "a"):
                                damage = player.base_atk + player.type.bonus_atk
                                goblin.hp -= damage
                                print(
                                    f"You dealt {damage} dmg to the {goblin.name}!\n")
                                if isinstance(player.type, Normal_Guy):
                                    if random.random() <= player.type.activation_chance:
                                        goblin.hp -= player.type.passive_dmg
                                        print(
                                            f"Your passive has activated, One Above All deals an extra {player.type.passive_dmg} dmg to the {goblin.name}!!\n")
                                    else:
                                        print("Passive failed to activate\n")

                            if goblin.hp <= 0:
                                goblin.reset()
                                print(
                                    f"\nYou defeated the {goblin.name}!!")
                                again = input(
                                    "Wanna continue adventuring? (y/n): ")
                                if again in ("yes", "y"):
                                    continue
                                elif again not in ("yes", "y"):
                                    break

                            elif goblin.hp > 0:

                                continue

                    elif choice in ("2", "inventory"):
                        print("inventory")

                    elif choice in ("3", "shop"):
                        print("shop")

                    elif choice in ("4", "exit", "exit game"):
                        break

                    else:
                        print("Invalid Action")
                        continue


game()
