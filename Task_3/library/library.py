from math import log


class Dragon:
    def __init__(self, color='black', health=100, is_alive=True):
        self.__color = color
        self.__health = health
        self.__is_alive = is_alive

    def bite(self):
        if self.__is_alive:
            self.__health += 10

    def get_damage(self, x: int):
        if log(x, 2) % 1 == 0:
            self.__health = 2 ** (int(log(self.__health, 2)) + 1)
            return
        self.__health -= x
        if self.__health <= 0:
            self.__is_alive = False

    def get_health(self) -> int:
        return self.__health
