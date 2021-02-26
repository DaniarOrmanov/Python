# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

class Storage:

    __data = {'принтер': 0, 'сканер': 0, 'копир': 0}
    __divisions = {1: 'конструкторское бюро', 2: 'Проектный отдел', 3: 'Бухгалтерия'}

    @staticmethod
    def take():
        for key in Storage.__data:
            Storage.__data[key] = int(input(f'Введите количество поступивших на склад {key}ов: '))
        print(f'На складе числится:')
        for key, volue in Storage.__data.items():
            print(f'{key.title()}: {volue} шт.')

    # def give(self):
        # print('Выберите отдел для передачи оргтехники:'
        # for key, volue in divisions.items():
        #     print(f'{key}. {volue.title}')
        # division = input('Введите номер отдела: ')
        # print(f'На складе числится:')
        # i = 0
        # for key, volue in data.items():
        #     print(f'{i}. {key.title()}: {volue} шт.')
        #     i += 1
        # while True:
        #     equip = input(f'Введите номер устройства для передачи в {division.lower()}? ')


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


Storage.take()
# Storage.give()

