# 3. Реализовать базовый класс Worker (работник), в
# котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных
# данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def __init__(self, name, surname, position, income):
        Worker.__init__(self, name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname + ', ' + self.position

    def get_total_income(self):
        salary = self._income.get('wage') + self._income.get('bonus')
        return f'Доход с учетом премии составляет {salary}.'


emp1 = Position('Daniar', 'Ormanov', 'Design Engineer', {"wage": 65000, "bonus": 20000})
print(f'\n{emp1.get_full_name()}')
print(emp1.get_total_income())

emp2 = Position('Ivan', 'Petrov', 'Artist', {"wage": 55000, "bonus": 32000})
print(f'\n{emp2.get_full_name()}')
print(emp2.get_total_income())