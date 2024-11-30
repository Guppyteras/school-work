class Vehicle:
    def __init__(self, color, doors, gas_powered):
        self.__color = self.__validate_color(color)
        self.__doors = self.__validate_doors(doors)
        self.__gas_powered = self.__validate_gas_powered(gas_powered)

    def __validate_color(self, color):
        allowed_colors = ["Red", "Orange", "Blue", "Yellow", "Black"]
        if color in allowed_colors:
            return color
        else:
            raise ValueError("Please choose another color. Only {} are allowed.".format(", ".join(allowed_colors)))
    
    def __validate_doors(self, doors):
        if doors in [2, 4, 5]:
            return doors
        else:
            raise ValueError("Amount of doors only come in, 2, 4, and 5!")
        
    def __validate_gas_powered(self, gas_powered):
        if isinstance(gas_powered, bool):
            return gas_powered
        else:
            raise ValueError("Only boolean values are accepted for Gas Powered!")
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = self.__validate_color(color)

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        self.__doors = self.__validate_doors(doors)

    def get_gas_powered(self):
        return self.__gas_powered

    def set_gas_powered(self, gas_powered):
        self.__gas_powered = self.__validate_gas_powered(gas_powered)

    def __str__(self):
        return "Vehicle{{color='{}', doors={}, gas_powered={}}}".format(self.__color, self.__doors, self.__gas_powered)

    def is_eco_friendly(self):
        return self.__doors == 2 and not self.__gas_powered 