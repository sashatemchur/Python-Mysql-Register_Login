import pymysql
from tkinter import messagebox
from tkinter import *

connection = pymysql.connect(
                                host='localhost',
                                database='register',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)
    
cursor = connection.cursor()

def register():
    login = input("Hello, enter your login: ")
    password = input("Enter your password: ")
    email = input("Hello, enter your email: ")
    phone = int(input("Hello, enter your phone: "))

    register1 = cursor.execute("SELECT login, password, email, phone FROM useregister WHERE login = '{}' AND password = '{}' AND email = '{}' AND phone = '{}'".format(login, password, email, phone))

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO useregister(login, password, email, phone) VALUES('{}', '{}', '{}', '{}')".format(login, password, email, phone))
        connection.commit()
        print('Information:' + 'Regestration completed!')
    else:
        print('Error:' + 'User is exist or wrong password')

def login():
    login = input("Hello, enter your login: ")
    password = input("Enter your password: ")
    email = input("Hello, enter your email: ")
    phone = int(input("Hello, enter your phone: "))

    register1 = cursor.execute("SELECT login, password, email, phone FROM useregister WHERE login = '{}' AND password = '{}' AND email = '{}' AND phone = '{}'".format(login, password, email, phone))

    if not cursor.fetchone():
        print('Error:' + "User missing or password is wrong.")
    else:
        print("Information:" + "Welcome")

enter = input("Enter you action (r or l): ")
if enter == 'r':
    register()
elif enter == 'l':
    login()

cursor.execute("select * from useregister")
data = cursor.fetchall()
print(data)
cursor.close()