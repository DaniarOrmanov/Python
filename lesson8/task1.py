# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date

class Date:

    def __init__(self, date_now):
        self.date_now = date_now

    @classmethod
    def date_to_number(cls, date_class):
        print(f'\nЧисло - {date_class.split("-")[0]}\nМесяц - {date_class.split("-")[1]}\nГод - {date_class.split("-")[2]}')

    @staticmethod
    def valid(date_static):
        months = {(1, 3, 5, 7, 8, 10, 12): 31, (4, 6, 9, 11): 30, (2,): 28}     # по количеству дней в месяце
        massiv = date_static.split('-')
        i = 0
        while i < len(massiv):
            massiv[i] = int(massiv[i])
            i += 1
        if massiv[2] % 4 == 0 and massiv[2] > 0:
            print(f'\n{massiv[2]} год високосный.')
        elif massiv[2] % 4 != 0 and massiv[2] > 0:
            print(f'\n{massiv[2]} год не високосный.')
        else:
            print('\nГод введен неверно!')
            quit()

        if massiv[1] >= 1 and massiv[1] <= 12:
            print('Месяц введен из разрешенного диапазона')
        else:
            print(f'{massiv[1]}-го месяца не существует!')
            quit()

        count = 0
        flag = 0
        for j in months:
            for k in j:
                if k == massiv[1] and count == 0 and massiv[0] >= 1 and massiv[0] <= 31:
                    print(f'Вы ввели {massiv[0]} число {massiv[1]}-го месяца. А вообще то в {massiv[1]}'
                          f'-ом месяце 31 день.')
                    flag = 1
                    break
                elif k == massiv[1] and count == 1 and massiv[0] >= 1 and massiv[0] <= 30:
                    print(f'Вы ввели {massiv[0]} число {massiv[1]}-го месяца. А вообще то в {massiv[1]}'
                          f'-ом месяце 30 дней.')
                    flag = 1
                    break
                elif k == massiv[1] and count == 2 and massiv[2] % 4 == 0 and massiv[0] >= 1 and massiv[0] <= 29:
                    print(f'Вы ввели {massiv[0]} число {massiv[1]}-го месяца. А вообще то в {massiv[1]}'
                          f'-ом месяце 29 дней.')
                    flag = 1
                    break
                elif k == massiv[1] and count == 2 and massiv[2] % 4 != 0 and massiv[0] >= 1 and massiv[0] <= 28:
                    print(f'Вы ввели {massiv[0]} число {massiv[1]}-го месяца. А вообще то в {massiv[1]}'
                          f'-ом месяце 28 дней.')
                    flag = 1
                    break
                else:
                    flag = 0
            count += 1
            if flag == 1:
                quit()
        if flag == 0:
            print('Число введено неверно!')
            quit()


my_date = '23-10-1989'
Date.date_to_number(my_date)
Date.valid(my_date)
