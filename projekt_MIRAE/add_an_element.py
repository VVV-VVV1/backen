import sqlite3
import datetime

now = datetime.datetime.now()
con = sqlite3.connect("server.db") 
cur = con.cursor()


def add_an_element():
    cur.execute ('''CREATE TABLE IF NOT EXISTS user (
        id integer,
        username text,
        password text,
        created_at text,
        updated_at text)''')

    con.commit()    

    cur.execute("SELECT * FROM user")
    count_user = (len(cur.fetchall()))

    date = []
    

    id_user = count_user + 1
    username = input("введите ваше имя: ")
    password = input("придумайте пароль: ")
    created_at = now.strftime("%d-%m-%Y %H:%M")
    updated_at = now.strftime("%d-%m-%Y %H:%M")

    date.append([id_user, username, password, created_at, updated_at])

    cur.executemany("INSERT INTO user VALUES (?, ?, ?, ?, ?)", date) 

    print("данные записаны\nваш id", id_user, "запомните его")
    con.commit()
    con.close()

