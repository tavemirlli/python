# Вариант 19. Создание базового класса "Животное" и его наследование для создания классов "Собака", "Кошка". В классе
# "Животное" будут общие методы, такие как "дышать" и "питаться", а классы наследники будут иметь свои уникальные
# методы и свойства такие как "гавкать" и "мурлыкать".

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дышит")

    def eat(self):
        print(f"{self.name} питается")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} гавкает")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} мурлыкает")

d = Dog('Щеночек')
c = Cat('Котенок')

d.breathe()
d.eat()
d.bark()

print()

c.breathe()
c.eat()
c.meow()
