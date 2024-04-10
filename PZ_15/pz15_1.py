# !/usr/local/bin/python
# coding: UTF-8
# Приложение грузовые перевозки для некоторой организации. БД должна содержать таблицу ПЕРЕВОЗКИ со следующей структурой
# записи: маршрут, фамилия водителя, дата отправки, прибытия, масса груза.
import sqlite3 as sq
from info_perevozki import info_items
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS perevozki")
    cur.execute("""CREATE TABLE perevozki(
    marshrut INTEGER NOT NULL,
    sername_voditelya TEXT NOT NULL,
    data_otpr DATA NOT NULL,
    data_prib DATA NOT NULL,
    massa_gruza INTEGER NOT NULL
    )""")
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO perevozki VALUES(?,?,?,?,?)", info_items)
print('\n','Команда SELECT: ')
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("SELECT sername_voditelya FROM perevozki WHERE massa_gruza<1000")
    res_1 = cur.fetchall()
    print(f'\n{res_1}')
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE data_otpr = '09.05.2024'")
    res_2 = cur.fetchall()
    print(res_2)
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("SELECT data_otpr, data_prib FROM perevozki WHERE sername_voditelya = 'Сергеев'")
    res_3 = cur.fetchall()
    print(res_3)
print('\n','Команда UPDATE: ')
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE perevozki SET data_otpr='29.05.2024' WHERE data_otpr='28.05.2024'")
    cur.execute("SELECT * FROM perevozki WHERE marshrut = 3")
    res_4=cur.fetchall()
    print(f'\n{res_4}')
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE perevozki SET massa_gruza = +200 WHERE massa_gruza >= 1000")
    cur.execute("SELECT * FROM perevozki")
    res_5=cur.fetchall()
    print(res_5)
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE perevozki SET marshrut = 8, sername_voditelya = 'Афанасьев' WHERE marshrut = 10")
    cur.execute("SELECT * FROM perevozki WHERE sername_voditelya = 'Афанасьев'")
    res_6=cur.fetchall()
    print(res_6)
print('\n','Команда DELETE: ')
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM perevozki WHERE marshrut = 1")
    cur.execute("SELECT * FROM perevozki")
    res_7=cur.fetchall()
    print(f"\n{res_7}")
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM perevozki WHERE sername_voditelya LIKE 'М%'")
    cur.execute("SELECT * FROM perevozki")
    res_8=cur.fetchall()
    print(res_8)
with sq.connect('gruzovie_perevozki.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM perevozki WHERE massa_gruza < 300")
    cur.execute("SELECT * FROM perevozki")
    res_9=cur.fetchall()
    print(res_9)


