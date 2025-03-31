"""
Создай класс Student (студент) с полями
- Имя (name) - строка
- Курс (course) - целое число
Создай два экземпляра
- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:

    def __init__(self, name: str, course: int):
        self.name = name
        self.course = course
