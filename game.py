

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


class Player:
    def __init__(self, name="", type=Hero):
        self.type = type
        self.name = name
        self.base_hp = 100
        self.base_atk = 10


master_swordsmen = Master_Swordsmen()
highclass_tanker = Highclass_Tanker()
spirit_archer = Spirit_Archer()
elemental_brawler = Elemental_Brawler()


heros = [master_swordsmen, highclass_tanker, spirit_archer, elemental_brawler]

player = None


def game():
    start_game = input("Do you wanna start a new adventure? (y/n): ").lower()
    player_name = input("NOW CHOOSE YOUR HEROS NAME!!!: ")
    player = Player(player_name)

    while True:
        if start_game not in ("yes", "y"):
            break

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

        choose_hero = int(input("Choose 1, 2, 3 or 4: "))

        if choose_hero == 1:
            player.type = master_swordsmen

        elif choose_hero == 2:
            player.type = highclass_tanker

        elif choose_hero == 3:
            player.type = spirit_archer

        elif choose_hero == 4:
            player.type = elemental_brawler


game()
