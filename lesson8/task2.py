# 2. Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class Exc:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exc_0(self):
        flag = 1
        try:
            num1 = float(self.num1)
            num2 = float(self.num2)
            result = num1 / num2
        except ValueError:
            print('Вы ввели не число!')
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')
        else:
            print(num1 / num2)


number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')

quot = Exc(number1, number2)
quot.exc_0()
