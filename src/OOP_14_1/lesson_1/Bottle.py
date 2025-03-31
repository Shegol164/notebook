"""
Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Объем (volume) - число с плавающей точкой

Создай три экземпляра

- Красную 0.7
- Белую 0.3
- Черную 1.0
"""


class Bottle:

    def __init__(self, color: str, volume: float) -> None:
        self.color = color
        self.volume = volume
