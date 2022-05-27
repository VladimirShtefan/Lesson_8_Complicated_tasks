from random import randint


class Dice:
    def __init__(self, facet: int):
        self.__facet = facet
        self.__history = []

    def dice_throw(self) -> int:
        dice_face = randint(1, self.__facet)
        self.__history.append(str(dice_face))
        return dice_face

    def get_history(self, x: int) -> list:
        return self.__history[:x]