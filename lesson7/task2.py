# 2. Реализовать проект расчета суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def cons(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def cons(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def cons(self):
        return 2 * self.height + 0.3


s = [5, 3, 6, 10]                      # размеры пальто
h = [3, 4, 2]                          # ростовки для костюмов
sum_coat = 0
sum_suit = 0

i = 0
while i < len(s):
    coat = Coat(s[i])
    sum_coat = sum_coat + coat.cons
    i += 1
print(f'Расход ткани на {len(s)} пальто равен {sum_coat:.2f}.')

i = 0
while i < len(h):
    suit = Suit(h[i])
    sum_suit = sum_suit + suit.cons
    i += 1
print(f'Расход ткани на {len(h)} костюм(-а, -ов) равен {sum_suit:.2f}.')

sum = sum_coat + sum_suit
print(f'Суммарный расход ткани на одежду равен {sum:.2f}.')
