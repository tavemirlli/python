# !/usr/local/bin/python
# coding: UTF-8
# Создать класс Person с одним атрибутом класса (count), с конструктором __init__ и одним статическим методом.
# Увеличение количества созданных экземпляров обеспечить в конструкторе __init__. Статический метод total_people
# должен обеспечивать построение и вывод фразы о количестве созданных экземпляров.

class Person:
    count = 0
    def __init__(self, name):
        Person.count += 1
        self.name = name

    @staticmethod
    def total_people():
        print(f"{Person.count} экземпляра(ов) создано.")

p2 = Person('lisa')
p3 = Person('Ivan')
Person.total_people()