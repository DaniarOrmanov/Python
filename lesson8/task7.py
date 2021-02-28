# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте
# работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте
# корректность полученного результата.

class Complex:

    def __init__(self, reim):
        self.reim = reim

    def __add__(self, other):
        return self.reim[0] + other.reim[0], self.reim[1] + other.reim[1]

    def __mul__(self, other):
        pass

    def print(self):
        print(self.reim)


number1 = Complex((1, 2))
number2 = Complex((3, -3))
# a = number1 + number2
# Complex.print(a)
Complex.print(number1)
Complex.print(number1 + number2)