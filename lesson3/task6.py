# 6. Реализовать функцию int_func(), принимающую слово из
# маленьких латинских букв и возвращающую его же, но с прописной первой
# буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из
# слов, разделенных пробелом. Каждое слово состоит из латинских букв в
# нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее
# функцию int_func().

def int_func(word, result):
    latin_flag = 0  # 1, если слово состоит только из латинских букв в нижнем регистре
    if word.isalpha() and word.islower():
        j = 0
        while j < len(word):
            if latin.find(f'{word[j]}', 0, len(latin)) != -1:
                latin_flag = 1
                j += 1
            else:
                j += 1
                latin_flag = 0
                break
        if latin_flag == 1:
            result = result + word.title() + ' '
    return result

result = ''
latin = 'abcdifghijklmnopqrstuvwxyz'
str = input('\nВведите одно или несколько слов в нижнем регистре'
            ' латиницей, отделяя их пробелами, и нажмите Enter: ')
list = str.split(' ')
i = 0
while i < len(list):
    word = list[i]
    result = int_func(word, result)
    i += 1

if result == '':
    print('Вы вводите что-то не то!! Попробуйте снова.')
else:
    print(f'\nВы ввели вот такую строку: "{str}".\nПрограмма выбрала все слова, написанные'
          f'в нижнем регистре латинскими буквами, и записала их с большой буквы:\n "{result[0:len(result)-1]}"')
