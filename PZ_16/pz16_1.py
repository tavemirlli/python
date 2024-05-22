# !/usr/local/bin/python
# coding: UTF-8
# Создайте класс "Студент", который имеет атрибуты имя, фамилия и оценки. Добавьте методы для вычисления среднего балла
# и определения, является ли студент отличником

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def sr(self):
        return sum(self.grades) / len(self.grades)

    def otl(self):
        return all(grade == 5 for grade in self.grades)

# Пример использования
student1 = Student("Алиса", "Мир", [5, 5, 5])
student2 = Student("Наташа", "Москов", [3, 4, 4, 4])
student3 = Student("Андрей", "Железный", [5, 5, 5, 4])

print(f"{student1.first_name} {student1.last_name} имеет средний бал равный {student1.sr()}")
print(f"{student2.first_name} {student2.last_name} имеет средний бал равный {student2.sr()}")
print(f"{student3.first_name} {student3.last_name} имеет средний бал равный {student3.sr()}")

print(f"\n{student1.first_name} {student1.last_name} является отличником: {student1.otl()}")
print(f"{student2.first_name} {student2.last_name} является отличником: {student2.otl()}")
print(f"{student3.first_name} {student3.last_name} является отличником: {student3.otl()}")


