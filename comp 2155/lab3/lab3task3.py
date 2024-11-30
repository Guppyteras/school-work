class Home:
    def __init__(self, address, price, size):
        self.__address = address
        self.__price = price
        self.__size = size

    # Private properties with accessors and mutators
    @property
    def _address(self):
        return self.__address

    @_address.setter
    def _address(self, value):
        self.__address = value

    @property
    def _price(self):
        return self.__price

    @_price.setter
    def _price(self, value):
        self.__price = value

    @property
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value