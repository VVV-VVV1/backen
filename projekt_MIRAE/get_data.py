import sqlite3
import datetime

now = datetime.datetime.now()
con = sqlite3.connect("server.db") 
cur = con.cursor()

def get_data():
    a = input("Вы хотите вывести all or one user?")

    if a == "all":
        cur.execute('SELECT * FROM user')

        rows = cur.fetchall()
        for row in rows:
            print(row)

        con.commit()
        con.close()
    if a == "one user":
        id = input("Введите id пользователя: ")

        one_user ="""SELECT username, password, created_at, updated_at FROM user WHERE id = ?"""
        cur.execute(one_user, id)
        
        rows = cur.fetchall()
        for row in rows:
            print(row)

        con.commit()
        con.close()