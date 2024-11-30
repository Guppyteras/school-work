from task1 import Vehicle

class Truck(Vehicle):
    def __init__(self, color, doors, gas_powered, seats, trunk_space):
        super().__init__(color, doors, gas_powered)
        self.__seats = self.__validate_seats(seats)
        self.__trunk_space = self.__validate_trunk_space(trunk_space)

    def __validate_seats(self, seats):
        if isinstance(seats, int) and seats > 0:
            return seats
        else:
            raise ValueError("Seats must be a positive integer.")

    def __validate_trunk_space(self, trunk_space):
        if isinstance(trunk_space, int) and trunk_space > 0:
            return trunk_space
        else:
            raise ValueError("Trunk space must be a positive integer.")

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = self.__validate_seats(seats)

    def get_trunk_space(self):
        return self.__trunk_space

    def set_trunk_space(self, trunk_space):
        self.__trunk_space = self.__validate_trunk_space(trunk_space)

    def __str__(self):
        return "Truck{{color='{}', doors={}, gas_powered={}, seats={}, trunk_space={}}}".format(self.get_color(), self.get_doors(), self.get_gas_powered(), self.__seats, self.__trunk_space)

    def is_eco_friendly(self):
        return super().is_eco_friendly() and self.__seats <= 2 and self.__trunk_space == 0
