from poo.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, qtd_doors: int, *args):
        super(Car, self).__init__(*args)
        self.qtd_doors = qtd_doors
        self._libras = 30  # atributo protegigio pode ser acessado apenas pelas classes filhas..

    def to_fuel(self, qtd_fuel: int):
        print('the method was called from the car class')
        self._qtd_fuel += qtd_fuel

    def to_paint(self, color: str):
        if color == "red":
            print("the car can't be red")
        self.color = color
