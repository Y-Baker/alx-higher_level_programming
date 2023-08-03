#!/usr/bin/python3

"""New Module for Student Class"""


class Student:
    """New Class Called Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize Emety Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
