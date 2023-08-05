#!/usr/bin/python3

"""Rectangle Module from Package Models"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize A new Rectangle
        Args:
        width: int
        height: int
        x: int
        y: int
        id: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return The Area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """print the shape of the Rectangle take care of x, y"""
        for _ in range(self.__y):
            print()
        for row in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for col in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        Update the Rectangle by a tupe of args
        OR: a dictinary of args as key: value
        """
        instance = ['id', '_Rectangle__width', '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        if args and len(args) > 0:
            for n, arg in enumerate(args):
                if n == 0 and arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                    continue
                self.__dict__[instance[n]] = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                new_key = "_Rectangle__" + key
                if new_key in self.__dict__:
                    self.__dict__[new_key] = value

    def to_dictionary(self):
        """Creat dict representation of Rectangle"""
        new_dict = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if key[:12] == "_Rectangle__":
                new_dict[key[12:]] = new_dict.pop(key)

        return new_dict

    def __str__(self):
        """Called when you try to print the opbject"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
