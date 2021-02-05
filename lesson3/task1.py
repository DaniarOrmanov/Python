# 1. Реализовать функцию, принимающую два числа (позиционные
# аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def div(num1, num2):
    return num1/num2

number = list()
words = ['делимое', 'делитель']
i = 0
while i < 2:
    enter = input(f'Введите {words[i]} - ')
    try:
        number.append(float(enter))
        i += 1
    except ValueError:
        if enter.lower() == 'q':
            quit()
        else:
            print(f'Вы ввели "{enter}", а это не число. Введите число еще раз.\nИли введите Q для выхода.')
if number[1] == 0:
    print('На ноль лучше не делить.')
else:
    result = div(number[0], number[1])
    print(f'Если разделить {number[0]} на {number[1]} - получится {result:.3f}.')


