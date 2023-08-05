#!/usr/bin/python3

"""Square Module from Package models"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize A new Square
        Args:
        size: int
        x: int
        y: int
        id: int
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of width"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Rectangle by a tupe of args
        OR: a dictinary of args as key: value
        """
        if args and len(args) > 0:
            if args[0] is None:
                self.__init__(self.size, self.x, self.y)
            if len(args) > 0 and args[0]:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Creat dict representation of square"""
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict

    def __str__(self):
        """Called when you try to print the opbject"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )
