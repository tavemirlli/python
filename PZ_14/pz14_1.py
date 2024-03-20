# !/usr/local/bin/python
# coding: UTF-8
# Из исходного файла (pazzl.html) выбрать все html-коды изображений. Посчитать их количество.

import re

# Открываем исходный файл и считываем его содержимое
with open('pazzl.html', 'r') as file:
    data = file.read()

# Используем регулярное выражение для поиска всех изображений
image_tags = re.findall(r'<img.*?>', data)
lines_as_lists = list(map(lambda x: x, image_tags))
numbered_lines = list(enumerate(lines_as_lists, start=1))
list(map(lambda x: print(f'{x[0]}: {x[1]}'), numbered_lines))

# Нахадом количество изображений
image_count = len(image_tags)

print(f"Количество html-кодов изображений: {image_count}")
