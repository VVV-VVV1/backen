import sqlite3
import datetime
import add_an_element
import changing_elements
import delete_user_or_table
import get_data

now = datetime.datetime.now()
con = sqlite3.connect("server.db") 

if __name__ =="__main__":
    print("В нашей базе данных можно create, update, delete и get")
    a = str(input("что вы хотите ? "))
    if a == "create":
        add_an_element.add_an_element()
    if a == "update":
        changing_elements.changing_elements()
    if a == "delete":
        delete_user_or_table.delete_user_or_table()
    if a == "get":
        get_data.get_data()




    
    
   

