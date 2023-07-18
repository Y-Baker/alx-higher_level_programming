#!/usr/bin/python3

"""New module"""


class Square:
    """Square opject"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): the size of the new sqare
            position (tuble (2 int)): the position of the new sqare
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter to size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter to the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to the position attribute"""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """print square by '#' by the size"""
        if self.__size == 0:
            print("")
            return

        for n in range(self.__position[1]):
            print()

        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(' ', end="")
            for col in range(self.__size):
                print('#', end="")
            print()
