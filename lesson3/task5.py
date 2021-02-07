# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def sum_func(my_sum, flag):
    """
    Функция нужна для ввода данных. Из всех введенных данных выбираются только действительны числа и суммируются.
    После ввода "q" программа завершается.
    :param my_sum: сумма введенных чисел
    :param flag: 1 - если были введены не числа
    :return: функция возвращает сумму всех введенных чисел
    """
    str = input('\nВведите несколько чисел, отделяя их пробелами, и нажмите Enter: ')
    list = str.split(' ')
    i = 0
    while i < len(list):
        try:
            float(list[i])
            my_sum = my_sum + float(list[i])
            i += 1
        except ValueError:
            word = list[i]
            if word.lower() == 'q':
                print(f'Сумма чисел до введения "q" равна {my_sum}')
                quit()
            else:
                i += 1
                flag = 1
    return my_sum

my_sum = 0
flag = 0                       # flag = 1, если было введено не число

while True:
    my_sum = sum_func(my_sum, flag)
    print(f'\nСумма введенных чисел равна {my_sum}')
    if flag == 1:
        print('\nКогда Вы вводите не число, а что-то другое, мы это просто пропускаем.')
    print('Если хотите выйти, то нажмите "q"')
