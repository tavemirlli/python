# !/usr/local/bin/python
# coding: UTF-8
# Из исходного файла (pazzl.html) выбрать все html-коды изображений. Посчитать их количество.

import re

# Открываем исходный файл и считываем его содержимое
with open("pazzl.html", "r") as file:
    data = file.read()

# Используем регулярное выражение для поиска всех изображений
image_tags = re.findall(r'<img.*?>', data)

# Нахадом количество изображений
image_count = len(image_tags)

print(f"Количество html-кодов изображений: {image_count}")
