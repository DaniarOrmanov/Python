# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass

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