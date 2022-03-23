from __future__ import annotations
from datetime import datetime
from random import randint
from typing import List
from xmlrpc.client import Boolean


class Student:

    __used_ids = []
    actual_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name: str, age: int, approved: Boolean = False) -> None:
        self.name = name
        self.age = age
        self.approved = approved

    def getBirthYear(self) -> int:
        return self.actual_year - self.age

    @classmethod
    def create_by_birth_year(cls, name: str, year: int) -> Student:
        return cls(name, cls.actual_year-year)

    @classmethod
    def generate_registration_id(cls) -> int:
        randId = randint(0, 99999)
        while randId in cls.__used_ids:
            randId = randint(0, 99999)
        return randId

    @classmethod
    @property
    def used_ids(self) -> List:
        return self.__used_ids

    #age getter
    @property
    def age(self) -> int:
        return self._age

    #age setter
    @age.setter
    def age(self, value: int) ->None:
        if not isinstance(value, int):
            raise TypeError("Not an integer")
        else:
            self._age = value