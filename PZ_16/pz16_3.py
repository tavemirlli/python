# !/usr/local/bin/python
# coding: UTF-8
# Для задачи из блока І создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземяров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации обьектов Python

import pickle
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
student1 = Student("Alice", "Smith", [5, 5, 5])
student2 = Student("Bob", "Johnson", [3, 4, 4, 4])
student3 = Student("Lisa", "Mariy", [5, 5, 5, 4])

print(f"{student1.first_name} {student1.last_name} имеет средний бал равный {student1.sr()}")
print(f"{student2.first_name} {student2.last_name} имеет средний бал равный {student2.sr()}")
print(f"{student3.first_name} {student3.last_name} имеет средний бал равный {student3.sr()}")

print(f"\n{student1.first_name} {student1.last_name} является отличником: {student1.otl()}")
print(f"{student2.first_name} {student2.last_name} является отличником: {student2.otl()}")
print(f"{student3.first_name} {student3.last_name} является отличником: {student3.otl()}")

print()
student1 = ["Alice", "Smith", [5, 5, 5]]
student2 = ["Bob", "Johnson", [3, 4, 4, 4]]
student3 = ["Lisa", "Mariy", [5, 5, 5, 4]]

def save_data(student, filename):
    with open(filename, 'wb') as file:
        pickle.dump(student, file)
        print(f"Data saved to {filename}")

def load_data(filename):
    with open(filename, 'rb') as file:
        student = pickle.load(file)
        return student

save_data(student1, "student1.bin")
save_data(student2, "student2.bin")
save_data(student3, "student3.bin")

loaded_student1 = load_data("student1.bin")
loaded_student2 = load_data("student2.bin")
loaded_student3 = load_data("student3.bin")

print('\n''Вывод из файла:', loaded_student1, loaded_student2, loaded_student3, sep='\n')