# Дана строка, состоящая из русских слов, разделенных пробелами(одним или несколькими). Вывести строку, содержащую эти
# же слова, разделенные одним пробелом и расположенные в обратном порядке.
s = input("Введите строку: ")
w = s.split() # разбивка символов
reversedw = ' '.join(reversed(w)) # возвращает слова с определенным разделителем
print('Слова, расположенные в обратном порядке: ', reversedw)