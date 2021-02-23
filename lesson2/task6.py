# 6. * Реализовать структуру данных «Товары». Она должна
# представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру
# нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение —
# список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

quantity = input(f'\nВведите количество товаров в структуре: ')
try:
    float(quantity)
except ValueError:
    print('Вы ввели не то.')
else:
    if float(quantity) > 0 and float(quantity) == int(quantity):
        quantity = int(quantity)
    else:
        print(f'Надо ввести натуральное число.')

catalog = list()
dict_data = {'название': None, 'цена': None, 'количество': None, 'ед.': None}
stat = dict_data                              # пустой словарь для вывода данных
stat_data = [[], [], [], []]
i = 0
while i < quantity:
    dict_data['название'] = input(f'Введите название {i + 1}-го товара: ')
    stat_data[0].append(dict_data['название'])
    dict_data['цена'] = input(f'Введите цену товара "{dict["название"]}": ')
    stat_data[1].append(dict_data['цена'])
    dict_data['количество'] = input(f'Введите количество товара "{dict["название"]}": ')
    stat_data[2].append(dict_data['количество'])
    dict_data['ед.'] = input(f'Введите единицы измерения товара "{dict["название"]}": ')
    stat_data[3].append(dict_data['ед.'])
    product = (i + 1, dict_data)
    catalog.append(product)
    i += 1

i = 0
for key in stat:
    stat[key] = stat_data[i]
    i += 1

print(stat.items())
