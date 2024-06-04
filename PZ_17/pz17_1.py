# !/usr/local/bin/python
# coding: UTF-8
# Вариант 19.В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

from tkinter import *

root = Tk()
root.geometry('800x900')
root.title('Регистрация')

frame1_1 = Frame(root, width=790, height=890)
frame1_1.place(x=5, y=5)
label2 = Label(root, text='Регистрация', fg='#00BCFF', font='Arial 20 bold')
label2.place(x=10, y=5)

frame1 = Frame(root, bg='#00BCFF', bd=5, width=770, height=50)
frame1.place(x=15,y=50)
label1 = Label(root, text='Создание нового сайта', fg='#FFFFFF', bg='#00BCFF', font='Arial 15 bold')
label1.place(x=290,y=60)

label3 = Label(frame1_1, text='Email', fg='#001AFF', font='Arial 13 bold')
label3.place(x=225,y=130)
entry1 = Entry(frame1_1, bg='white', width=50)
entry1.place(x=280,y=130)

label4 = Label(frame1_1, text='Пароль', fg='#001AFF', font='Arial 13 bold')
label4.place(x=205,y=170)
frame2 = Frame(frame1_1, bg='#C4C4C4', width=770)
frame2.place(x=10,y=220)
entry2 = Entry(frame1_1, bg='white', width=50)
entry2.place(x=280,y=170)

label5 = Label(frame1_1, text='Имя', fg='#001AFF', font='Arial 13 bold')
label5.place(x=230,y=260)
entry3 = Entry(frame1_1, bg='white', width=50)
entry3.place(x=280,y=260)

label6 = Label(frame1_1, text='Фамилия', fg='#001AFF', font='Arial 13 bold')
label6.place(x=190,y=300)
entry4 = Entry(frame1_1, bg='white', width=50)
entry4.place(x=280,y=300)

label7 = Label(frame1_1, text='Никнейм', fg='#001AFF', font='Arial 13 bold')
label7.place(x=193,y=340)
entry5 = Entry(frame1_1, bg='white', width=50)
entry5.place(x=280,y=340)

label8 = Label(frame1_1, text='Дата рождения', fg='#001AFF', font='Arial 13 bold')
label8.place(x=140,y=410)
data = 1
data1 = 2
var = StringVar()
menu = OptionMenu(frame1_1, var, data, data1 )
menu.grid(row=1, column=1)
menu.place(x=280,y=410)
data2 = 'январь'
data3 = 'февраль'
var1 = StringVar()
menu1 = OptionMenu(frame1_1, var1, data2, data3 )
menu1.grid(row=1, column=1)
menu1.place(x=350,y=410)
data4 = 2005
data5 = 2006
var2 = StringVar()
menu2 = OptionMenu(frame1_1, var2, data4, data5 )
menu2.grid(row=1, column=1)
menu2.place(x=420,y=410)

frame3 = Frame(frame1_1, bg='#C4C4C4', width=770)
frame3.place(x=10,y=390)

label8 = Label(frame1_1, text='Пол', fg='#001AFF', font='Arial 13 bold')
label8.place(x=230,y=460)
var = IntVar()
chek = Radiobutton(frame1_1, text='Муж', variable=var, value=1)
chek.place(x=280,y=460)
chek1 = Radiobutton(frame1_1, text='Жен', variable=var, value=2)
chek1.place(x=350,y=460)

label9 = Label(frame1_1, text='Место проживания', fg='#001AFF', font='Arial 13 bold')
label9.place(x=110,y=490)
data6 = 'Москва'
data7 = 'Ростов-на-Дону'
var3 = StringVar()
menu3 = OptionMenu(frame1_1, var2, data6, data7)
menu3.grid(row=1, column=1)
menu3.place(x=350,y=490)

frame3 = Frame(frame1_1, bg='#C4C4C4', width=770)
frame3.place(x=10,y=540)

label10 = Label(frame1_1, text='Код безопасности', fg='#001AFF', font='Arial 13 bold')
label10.place(x=115,y=570)
entry6 = Entry(frame1_1, bg='white', width=20)
entry6.place(x=280,y=570)
label11 = Label(frame1_1, text='CFhUJ77', fg='Black', font='Arial 20 bold', bg='#D2D2D2')
label11.place(x=430,y=570)

box = Checkbutton(frame1_1, text='Подтверждаю', font='Arial 13' )
box.place(x=280,y=620)
label12 = Label(frame1_1, text='условия использования', font='Arial 13 underline', fg='#001AFF')
label12.place(x=420,y=622)
label13 = Label(frame1_1, text='uID сообщества',font='Arial 13')
label13.place(x=620,y=622)

label14 = Label(frame1_1, text='Мы гарантируем конфидинциальность информации, она в надежных руках',
                font='Arial 12 bold', fg='#C4C4C4')
label14.place(x=120,y=655)

but = Button(frame1_1, bg='#00BCFF', width=20, height=1, text='Регистрация', fg='white', font='Arial 16 bold')
but.place(x=120,y=695)

root.mainloop()
