import random

blessings = [
    {
        "id": "Athena",
        "name": "War of the mind",
        "stat_increase": (10)
    },

    {
        "id": "Hades",
        "name": "Commander of the dead",
        "stat_increase": (10)
    },

    {
        "id": "Eirene",
        "name": "The peacekeeper",
        "stat_increase": (10)
    },

    {
        "id": "Hyperion",
        "name": "Radiance of the one true sun god",
        "stat_increase": (10)
    }
]


class Player:
    def __init__(self, name=""):
        self.name = name
        self.base_hp = 100
        self.base_atk = 10


class Heros:
    def __init__(self, bonus_hp, bonus_atk, hero_type="", true_name=""):
        self.__true_name = true_name
        self.hero_type = hero_type
        self.bonus_hp = bonus_hp
        self.bonus_atk = bonus_atk


class Master_Swordsmen(Heros):
    def __init__(self, sword_blessing, bonus_hp, bonus_atk, hero_type, true_name):
        self.sword_blessing = sword_blessing
        super().__init__(bonus_hp, bonus_atk, hero_type, true_name)

    def blessing(self):
