# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число: ')

number1 = int(number)
number2 = int(number + number)
number3 = int(number + number + number)
sum = number1 + number2 + number3

print(f'Сумма n + nn + nnn = {sum}')

