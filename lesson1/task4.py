# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите число: ')    # ввод числа

if int(number) > 0:
    count = len(number)                  # количество цифр в числе
    max = 0                              # пока максимальная цифра равна 0

    i = 0
    while i < count:
        if max < int(number[i]):
            max = int(number[i])
            i = i + 1
        else:
            i = i + 1
    print(f'Самая большая цифра в числе {number} - это "{max}"')
else:
    print(f'{number} - это не целое положительное число')








