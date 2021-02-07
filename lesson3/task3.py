# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def enter():
    """
    Вводятся числа и возвращаются в виде списка. Если ввели не число, то выводится сообщение.
    :return: массив введенных чисел
    """
    i = 0
    while i < len(words):
        enter = input(f'Введите {words[i]} аргумент - ')
        try:
            numbers.append(float(enter))
            i += 1
        except ValueError:
            if enter.lower() == 'q':
                quit()
            else:
                print(f'Вы ввели "{enter}", а это не число. Введите число еще раз.\nИли введите Q для выхода.')
    return numbers

def my_func(a, b, c):
    """
    Функция находит сумму двух наибольших чисел из трех
    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма двух наибольших
    """
    massiv = [a, b, c]
    massiv.sort()
    sum_max = massiv[-2] + massiv[-1]
    return sum_max

numbers = list()
words = ['первый', 'второй', 'третий']
numbers = enter()
result = my_func(numbers[0], numbers[1], numbers[2])
print(f'Сумма двух наибольших чисел равна {result:.3f}.')
