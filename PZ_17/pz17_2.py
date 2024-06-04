# Вариант 19. Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.
# ПЗ№3 Вариант 19. Проверить истинность высказывания: "Среди данных трех целых чисел есть хотя бы одна пара
# совпадающих

from tkinter import *
from tkinter import messagebox

def sravnenie():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        c = int(entry3.get())
        if a == b or b == c or c == a:
            (messagebox.showinfo
             (message="""Высказывание: "Среди данных трех целых чисел есть хотя бы одна пара совпадающих": ИСТИННО"""))
        else:
            (messagebox.showinfo
             (message="""Высказывание: "Среди данных трех целых чисел есть хотя бы одна пара совпадающих": ЛОЖНО"""))
    except:
        messagebox.showinfo(message='Ошибка ввода')

root = Tk()
root.geometry('300x400')
label1 = Label(text="Целое число А:")
entry1 = Entry(width=30)

label2 = Label(text="Целое число B:")
entry2 = Entry(width=30)

label3 = Label(text="Целое число C:")
entry3 = Entry(width=30)

button1 = Button(text='Проверить', command=sravnenie, bg='#FF80C9')

label1.place(x=70, y=40)
entry1.place(x=70, y=60)
label2.place(x=70, y=80)
entry2.place(x=70, y=100)
label3.place(x=70, y=120)
entry3.place(x=70, y=140)
button1.place(x=70, y=170)

root.mainloop()