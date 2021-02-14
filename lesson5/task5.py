# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.

with open('data5.txt', '+w') as data:
    numbers = input('Введите набор чисел, разделяя их пробелами: ')
    flag = 0
    for i in numbers.split(' '):
        try:
            float(i)
            data.write(i)
            data.write(' ')
            flag = 1
        except ValueError:
            pass
    if flag == 0:
        print('Вы не ввели ни одного числа!')

    data.seek(0)
    massiv = data.read()[:-1].split(' ')
    j = 0
    sum = 0
    while j < len(massiv):
        sum = sum + float(massiv[j])
        j += 1
    print(f'Сумма введенных чисел равна {sum}.')