"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""
from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        name_age = f"{self.name} is {self.age} years old"
        print(name_age)

    @classmethod
    def from_birth_year(cls, name, birth_year):
        cls.current_year = datetime.now().year
        age = cls.current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False
