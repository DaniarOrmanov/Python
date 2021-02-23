# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

year = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month = input('Введите номер месяца - ')
try:
    float(month)
except ValueError:
    print('Вы ввели не то.')
else:
    if float(month) > 0 and float(month) <= 12 and float(month) == int(month):
        month = int(month)
        flag = 0
        for key, volue in year.items():
            for i in volue:
                if i == month:
                    flag = 1
                    break
            if flag == 1:
                break
        print(f'{month}-й месяц - это {key}.')
    else:
        print('Надо ввести целое число от 1 до 12.')





