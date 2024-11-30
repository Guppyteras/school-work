class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.__title = title

    # Public properties
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Private property
    @property
    def _title(self):
        return self.__title