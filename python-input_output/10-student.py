#!/usr/bin/python3
"""
This module defines a class student
Attribute:
    first_name
    last_name
    age
Method:
    to_json that recieves a dictionary
    representation of student
"""


class Student:
    """
    This class defines a tudent
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return student representation of student"""
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)
                    }
        return self.__dict__
