"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""
import math


class Rectangle:
    def __init__(self, width, height) -> None:
        '''конструктор, принимающий ширину и высоту прямоугольника'''
        self.width = width
        self.height = height

    def area(self) -> None:
        '''метод, возвращающий площадь прямоугольника'''
        area = self.width * self.height
        return area

    def perimeter(self) -> None:
        '''метод, возвращающий периметр прямоугольника'''
        perimeter = 2 * (self.width + self.height)
        return perimeter

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        height = diagonal / math.sqrt(aspect_ratio ** 2 + 1)
        width = aspect_ratio * height
        return cls(width, height)

    @staticmethod
    def is_square(width, height):
        return width == height
