# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте
# механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:
    __names = {1: 'принтер', 2: 'сканер', 3: 'копир'}
    __data = dict()
    __names_count = 0
    for i in __names.values():
        __data[i] = 0                           # словарь вида {'принтер': 0, 'сканер': 0...}, где ключи соответствуют значениям словаря __names
        __names_count += 1
    __divisions = {1: 'Конструкторское бюро', 2: 'Проектный отдел', 3: 'Бухгалтерия'}
    __div_count = 0                        # количество отделов
    for i in __divisions:
        __div_count += 1

    @staticmethod
    def __output():
        """
        Метод выводит остаток на складе
        :return:
        """
        print(f'\nОстаток на складе:')
        i = 0
        for key, volue in Storage.__data.items():
            print(f'{i + 1}. {key.title()}: {volue} шт.')
            i += 1

    @staticmethod
    def __output_division():
        """
        Метод выводит список отделов
        :return:
        """
        for key, volue in Storage.__divisions.items():
            print(f'{key}. {volue}')

    @staticmethod
    def __check_quant(input_el):
        """
        Метод проверяет параметр input_el и возвращает сам параметр и флаг, показывающий, что было введено: "q" - для
        выхода из программы; "*" - для подъема вверх в меню; любая строка; произвольное число или подходящее
        целое неотрицательное число.
        :param input_el:
        :return:
        """
        try:
            float(input_el)
        except ValueError:
            if input_el == 'q':
                quit()
            elif input_el == '*':
                flag = 1                                     # введен символ '*'
                return input_el, flag
            else:
                flag = 2                                     # введена произвольная строка
                return input_el, flag
        else:
            if float(input_el) == int(float(input_el)) and int(float(input_el)) >= 0:
                flag = 4                                     # введено подходящее число
                return int(input_el), flag
            else:
                flag = 3                                     # введено произвольное число
                return float(input_el), flag

    @staticmethod
    def take():
        """
        Метод служит для ввода поступивших на склад устройств
        :return:
        """
        for key in Storage.__data:
            while True:
                quantity = input(f'Введите количество поступивших на склад {key}ов: ')
                output_check = Storage.__check_quant(quantity)
                if output_check[1] == 4:
                    Storage.__data[key] = output_check[0]
                    break
                else:
                    print('Надо ввести целое неотрицательное число!')
        Storage.__output()

    @staticmethod
    def give():
        """
        Метод служит для передачи устройст в выбранный отдел. Можно выбрать отдел, устройство и количество.
        Также выводится остаток на складе после каждой операции.
        :return:
        """
        while True:
            print('\nВыберите отдел для передачи оргтехники:')
            Storage.__output_division()                                                 # список всех отделов
            while True:
                division = input('Для выхода нажмите "q" или введите номер отдела: ')
                output_check = Storage.__check_quant(division)
                if output_check[1] == 4 and output_check[0] > 0 and output_check[0] <= Storage.__div_count:
                    division = output_check[0]
                    break
                else:
                    print(f'Имеется всего {Storage.__div_count} отдел(-а, -ов).')
            Storage.__output()                                                          # остаток на складе оргтехники
            j = 0
            while True:
                if j == 0:
                    equip = input(f'\nДля выхода нажмите "q";'
                                  f'\nДля смены отдела нажмите "*";'
                                  f'\nВведите номер устройства для передачи в отдел "{Storage.__divisions[int(division)]}": ')
                    output_check = Storage.__check_quant(equip)
                    if output_check[1] == 4 and output_check[0] > 0 and output_check[0] <= Storage.__names_count:
                        equip = output_check[0]
                        while True:
                            count = input(f'Введите количество передаваемых в отдел "{Storage.__divisions[int(division)]}" '
                                              f'{Storage.__names[int(equip)]}ов: ')
                            output_check = Storage.__check_quant(count)
                            if output_check[1] == 4:
                                count = output_check[0]
                                Storage.__data[Storage.__names[int(equip)]] -= count
                                print(f'\nВ отдел "{Storage.__divisions[int(division)]}" переданы {Storage.__names[int(equip)]}ы в '
                                      f'количестве {count} шт.')
                                Storage.__output()
                                break
                            else:
                                print('Надо ввести целое неотрицательное число!')
                    elif output_check[1] == 1:
                        break
                elif j == 1:
                    break


class OfficeTech:

    def __init__(self, year, price, brand, state='new', form='A4'):
        self.year = year
        self.price = price
        self.brand = brand
        self.form = form
        self.state = state

class Printer(OfficeTech):

    def __init__(self, color='цветной', func='струйный'):
        self.color = color

        self.func = func

class Scanner(OfficeTech):

    def __init__(self, resolution, slide='нет'):
        # resolution - разрешение изображения
        # slide - сканирование пленки
        self.resolution = resolution
        self.slide = slide

class Copier(OfficeTech):

    def __init__(self, speed, color='цветной'):
        self.speed = speed
        self.color = color


Storage.take()                      # Поступление на склад устройств
Storage.give()                      # Передача устройст в отделы