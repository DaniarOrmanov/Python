# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

before_mix = list()
after_mix = list()
number = input('Введите количество элементов в списке - ')
if type(number) is int and int(number) > 0:
    pass
else:
    print('Введите количество элементов в списке - ')


i = 0
while i < int(number):
    element = input('Введите элемент списка - ')
    before_mix.insert(i, element)
    if i % 2 == 0 and i != int(number)-1:
        after_mix.insert(i + 1, element)
    elif i % 2 != 0:
        after_mix.insert(i - 1, element)
    else:
        after_mix.insert(i, element)
    i += 1

print(before_mix, after_mix)