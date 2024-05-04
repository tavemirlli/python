# !/usr/local/bin/python
# coding: UTF-8
# Создайте класс "Студент", который имеет атрибуты имя, фамилия и оценки. Добавьте методы для вычисления среднего балла
# и определения, является ли студент отличником

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

def sr(student):
    return sum(student.grades) / len(student.grades)


def otl(student):
    for grade in student.grades:
        if grade < 5:
            return False
    return True

# Пример использования
student1 = Student("Alice", "Smith", [5, 5, 5])
student2 = Student("Bob", "Johnson", [3, 4, 4, 4])
student3 = Student("Lisa", "Mariy", [5, 5, 5, 4])

print(f"{student1.first_name} {student1.last_name} имеет средний бал равный {sr(student1)}")
print(f"{student2.first_name} {student2.last_name} имеет средний бал равный {sr(student2)}")
print(f"{student3.first_name} {student3.last_name} имеет средний бал равный {sr(student3)}")

print(f"\n{student1.first_name} {student1.last_name} является отличником: {otl(student1)}")
print(f"{student2.first_name} {student2.last_name} является отличником: {otl(student2)}")
print(f"{student3.first_name} {student3.last_name} является отличником: {otl(student3)}")


