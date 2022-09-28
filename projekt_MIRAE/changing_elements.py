import sqlite3
import datetime

now = datetime.datetime.now()
con = sqlite3.connect("server.db") 
cur = con.cursor()

def changing_elements():

    print("что вы хотите изменить name or pasword?")
    a = input()

    if a == "name":
        id = input("введите ваш id: ")
        username = input("введите новое имя: ") 
        updated_at = now.strftime("%d-%m-%Y %H:%M")

        update = """Update user set username = ?, updated_at = ? where id = ?"""

        data = (username, updated_at, id)
        cur.execute(update, data)

        print("Данные обновлены")

        con.commit()
        con.close()
    if a == "pasword":
        id = input("введите ваш id: ")
        password = input("введите новое имя: ") 
        updated_at = now.strftime("%d-%m-%Y %H:%M")

        update = """Update user set password = ?, updated_at = ? where id = ?"""

        data = (password, updated_at, id)
        cur.execute(update, data)

        print("Данные обновлены")

        con.commit()
        con.close()


    

