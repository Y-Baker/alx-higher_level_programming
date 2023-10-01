#!/usr/bin/pyhton3

"""Base Module in Package models"""
import json
import csv
import turtle


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base Object
        Args:
        id: int
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw the rectangle and squares with turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor('#88888')
        turt.pensize(5)
        turt.shape("turtle")

        turt.color("#e31414")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for _ in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()
        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """from python object to json str"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """write json str of list of py-object to a file"""
        if list_objs is None:
            list_dict = []
        else:
            list_dict = [_.to_dictionary() for _ in list_objs]
        json_str = cls.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """from json str to py object"""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create New Object By dict"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                object_created = cls(1, 2)
            elif cls.__name__ == "Square":
                object_created = cls(1)
            object_created.update(**dictionary)
            return object_created

    @classmethod
    def load_from_file(cls):
        """
        load json representation from <cls>.json file
        then convert it to py list of dictinary as
        each on represent an object
        then create an instance object form each dict in the list
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                json_str = f.read()
        except FileNotFoundError:
            return []
        list_dict = cls.from_json_string(json_str)
        list_obj = [cls.create(**_) for _ in list_dict]
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
