# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

year = {1: [1, 2, 12], 2: [3, 4, 5], 3: [6, 7, 8], 4: [9, 10, 11]}
print(year)
month = int(input('Введите номер месяца - '))
# threes = year.values()
# print(threes)
for i in year.values():
    three = i
    for j in three:
        if j == month:
            season = i
            print(season)


for i in year:
    # if i == season:
        print(i)
    # break






