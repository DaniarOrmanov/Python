# 7. Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в
# расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
#  {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import io
import json

i = 0
summa = 0
dict_company = {}
dict_m = {}
with io.open('data7.txt', encoding='utf-8') as data7:
    for company_data in data7:
        company_name = company_data[:company_data.find(' ')]
        company_data = company_data[company_data.find(' '):company_data.find('.')]
        company_data = company_data.split(' ')[2:]
        profit = float(company_data[0])-float(company_data[1])
        dict_company[company_name] = profit
        if profit >= 0:
            i += 1
            summa = summa + profit
    profit_m = summa/i
    dict_m['Прибыль'] = profit_m
    list_data = [dict_company, dict_m]
    print(f'\nСредняя прибыль по компаниям, получившим прибыль: {profit_m:.2f} рублей.')
    print('Список, состоящий из двух словарей: все компании и их прибыли/убытки, средняя прибыль компаний, получивших прибыль:')
    print(list_data)

with io.open('data_J.json', 'w') as data_J:
    json.dump(list_data, data_J)
