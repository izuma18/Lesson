from datetime import datetime as dt


class Player:
    __LVL__, __HEALTH__ = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL__
        self.__health = Player.__HEALTH__
        self.__born = dt.now()

    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL__ = Player.__typeTest(lvl)
        cls.__HEALTH__ = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Must be int')