class Person:
    def __init__(self, name):
        self.__name = name
    def age(self, age):
        if type(age) is int:
            if age < 15:
                return 'Молодой'
            if 15 < age <= 45:
                return 'Взрослый'
            if 30 < age <= 45:
                return 'Средний'
            if 45 < age <= 60:
                return 'Зрелый'
            else: return 'Пожилой'
        else: return 'Ошибка'
    def name(self):
        return self.__name
people = Person('Ruslan')
print(people.age(20))
print(people.name())
