from math import log


class Hero:
    def __init__(self, name: str):
        self.__experience = 0
        self.__name = name
        self.__health = 100
        self.__level = 1

    @staticmethod
    def get_lvl_for_exp(exp: int) -> int:
        return int(log(4 * exp / 15, 2))

    @staticmethod
    def get_health_for_lvl(lvl: int) -> int:
        health = 100
        for _ in range(lvl - 1):
            if (health / 2) % 10 != 0:
                health += int(health / 2 + 10 - (health / 2) % 10)
            else:
                health += int(health / 2)
        return health

    def add_experience(self, exp: int):
        self.__experience += exp
        self.__level = Hero.get_lvl_for_exp(self.__experience)
        self.__health = Hero.get_health_for_lvl(self.__level)

    def get_level(self) -> int:
        return self.__level

    def get_health(self) -> int:
        return self.__health


