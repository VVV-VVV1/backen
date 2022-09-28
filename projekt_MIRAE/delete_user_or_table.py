import sqlite3
import datetime

now = datetime.datetime.now()
con = sqlite3.connect("server.db") 
cur = con.cursor()

def delete_user_or_table():
    print("Что вы хотите удалить user or table? ")
    a = input()

    if a == "user":
        id = input("введите id, человека которого хотите удалить: ")

        update = """Update user set id = "####", username = "####", password = "####", created_at = "####", updated_at = "####" where id = ?"""
        
        data = (id)
        cur.execute(update, data)

        print("Данные уалены")

        con.commit()
        con.close()
    if a == "table":
        cur.execute('DROP TABLE IF EXISTS user')
        print("Данные уалены")

        con.commit()
        con.close()


