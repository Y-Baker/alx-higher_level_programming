#!/usr/bin/python3

"""New Module for Student Class"""


class Student:
    """New Class Called Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize Emety Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return Dictinart representation"""
        if (type(attrs) == list and
            all(type(element) == str for element in attrs)):
            new_dict = dict()
            for attr in sorted(attrs):
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
