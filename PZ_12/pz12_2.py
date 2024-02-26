# !/usr/local/bin/python
# coding: UTF-8
# Вариант 19. Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def str_to_lower(crs: str): # аргумент должен быть строкой
    for i in crs:
        yield i.upper()

user_str = input('Введите символы: ')
print(''.join(str_to_lower(user_str)))