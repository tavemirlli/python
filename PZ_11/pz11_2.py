# !/usr/local/bin/python
# coding: UTF-8
# Из предложенного текстового файла (18-19.txt) вывести на экран его
# содержимое, количество символов, принадлежащих
# к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме, предварительно
# заменив символы верхнего регистра на нижний.

with open('text18-19.txt', 'r', encoding='utf-16') as file:
    content = file.read()
print(content)

file11_2 = 'text18-19.txt'
count = 0
with open(file11_2, 'r') as file:
    filer = file.read()
    for char in filer:
        if char.isalpha():  # Проверяем, является ли символ буквой
            count += 1
print("Количество буквенных символов в файле:", count)

text_lower = content.lower()

lines = text_lower.split('\n')
poem = '\n\n'.join(' '.join(lines[i:i+1])
                   for i in range(0, len(lines)))

with open('poem.txt', 'w') as file:
    file.write(poem)

