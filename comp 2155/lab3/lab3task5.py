from lab3task3 import Home  # Import the Home class

class Apartment(Home):
    def __init__(self, address, price, size, num_bedrooms, num_bathrooms):
        super().__init__(address, price, size)
        self.__num_bedrooms = num_bedrooms
        self.__num_bathrooms = num_bathrooms

    # Private properties with accessors and mutators
    @property
    def _num_bedrooms(self):
        return self.__num_bedrooms

    @_num_bedrooms.setter
    def _num_bedrooms(self, value):
        self.__num_bedrooms = value

    @property
    def _num_bathrooms(self):
        return self.__num_bathrooms

    @_num_bathrooms.setter
    def _num_bathrooms(self, value):
        self.__num_bathrooms = value

    def __str__(self):
        return f"Apartment at {self._address} with {self._size} sqft, priced at ${self._price:.2f}, " \
               f"having {self._num_bedrooms} bedrooms and {self._num_bathrooms} bathrooms"