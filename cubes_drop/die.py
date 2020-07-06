from random import randint


class Die:
    """Класс, преддставляющий один кубик"""

    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число в зависимости от числа граней"""
        return randint(1, self.num_sides)