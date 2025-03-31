"""
Создай класс `Number` c полем `value` (указывается при инициализации)
Создай экземпляр, например `x = Number(7)`
Добавь методы:
`.get()` возвращает текущее value
`.add(<значение>)` добавляет указанное число к value
`.substract(<значение>)` вычитает указанное число из value
"""


class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, n):
        self.value += n

    def substract(self, n):
        self.value -= n
