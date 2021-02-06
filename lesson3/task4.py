# 4. Программа принимает действительное положительное число
# x и целое отрицательное число y. Необходимо выполнить возведение числа
# x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень. Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **. Второй — более
# сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    result = base ** exp
    return result

def my_func2(x, y):
    i = 0
    result = base
    while i < abs(y) - 1:
        result = result * base
        i += 1
    result = 1/result
    return result

words = ['действительное положительное', 'целое отрицательное']

i = 0
while i < 2:
    enter = input(f'Введите {words[i]} число: ')
    try:
        float(enter)
        good = 1
    except ValueError:
        good = 0
    if i == 0 and good == 1:
        if float(enter) > 0:
            base = float(enter)
            i += 1
        else:
            print('Вы ввели не то, что надо. Для выхода можете ввести "q" или снова')
    elif i == 1 and good == 1:
        if float(enter) == float(enter) // 1 and float(enter) < 0:
            exp = int(enter)
            i += 1
        else:
            print('Вы ввели не то, что надо. Для выхода можете ввести "q" или снова')
    elif good == 0:
        if enter.lower() == 'q':
            quit()
        else:
            print('Вы ввели не то, что надо. Для выхода можете ввести "q" или снова')

result1 = my_func1(base, exp)
result2 = my_func2(base, exp)
print(f'\nРезультаты возведения числа {base} в степень {exp}:')
print(f'Первая функция: {result1}\nВторая функция: {result2}')
