# from abc import abstractclassmethod, ABC
from poo.interface import Interface

class Vehicle(Interface):
    """
        this class vehicle , class used to inheritance between child classes.
    """

    def __init__(self, color: str, type_fuel: str, power: int):
        self.__color = color
        self.__type_fuel = type_fuel
        self.__power = power
        self._qtd_fuel: int = 0     # atributo protegido
        self.__is_on: bool = False
        self.__velocity: int = 0
        self._libras = 0        # diferente do atributo com 2 (underscore - private), 1 significa protected, logo somente as classes filhas poderão ter acesso.

    def __del__(self):
        print('object has been removed from memory!')

    # abastercer
    def to_fuel(self, qtd_fuel: int):
        """
        :param qtd_fuel: responsible for increasing a certain amount of fuel
        :return:
        """
        self._qtd_fuel += qtd_fuel

    # ligar
    def turn_on(self):
        if self.__is_on:
            print('the vehicle is already on!!!')
        else:
            self.__is_on = True
            print('the vehicle is on!')

    def turn_off(self):
        if not self.__is_on:
            print('the vehicle is already off!!')
        else:
            self.__is_on = False
            print('the vehicle is off')

    def speed_up(self, velocity: int = 10):
        if self.__is_on:
            self.__velocity += velocity
        else:
            print('to speed up the vehicle needs to be on!!')

    def to_paint(self, color: str):             # encapsulamento....
        self.__color = color
        print("The vehicle is color: %s" % color)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def verify_batery(self):
        pass

    def verify_board_computer(self):
        pass
