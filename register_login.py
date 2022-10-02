import mysql.connector
from tkinter import messagebox
from tkinter import *


connection = mysql.connector.connect(host='localhost',
                                database='register',
                                user='root',
                                password='') # Connect to the database 

cursor = connection.cursor()


def register(login, password, email, phone):
    
    output_table = cursor.execute("SELECT login, password, email, phone FROM useregister WHERE login = '{}' AND password = '{}' AND email = '{}' AND phone = '{}'".format(login, password, email, phone)) # Outputs data from the table according to the specified parameters

    if cursor.fetchone() is None: # If the displayed text is from the table, then fill in the following code
        cursor.execute("INSERT INTO useregister(login, password, email, phone) VALUES('{}', '{}', '{}', '{}')".format(login, password, email, phone)) # Writes data into a table
        connection.commit()
        return 'Information:' + 'Regestration completed!'
    else:
        return 'Error:' + 'User is exist or wrong password'


def login(login, password, email, phone):

    output_table = cursor.execute("SELECT login, password, email, phone FROM useregister WHERE login = '{}' AND password = '{}' AND email = '{}' AND phone = '{}'".format(login, password, email, phone)) # Outputs data from the table according to the specified parameters

    if not cursor.fetchone(): # If there is no displayed text from the table, then fill in the following code
        return 'Error:' + "User missing or password is wrong."
    else:
        return "Information:" + "Welcome"

enter = input("Enter you action (r or l): ")
if enter == 'r': # If r is selected, fill in the following code
    register()
elif enter == 'l': # If l is selected, fill in the following code
    login()
elif enter == '':
    print("An empty string is not allowed")
else:
    print("Choose r or l and not something else")

cursor.execute("SELECT * FROM useregister") # Select all from the table
output_all_table = cursor.fetchall() # Output everything from the table in text form
print(output_all_table)
cursor.close()
connection.close()

print(register(input("Hello, enter your login: "), input("Enter your password: "), input("Hello, enter your email: "), int(input("Hello, enter your phone: "))), login(input("Hello, enter your login: "), input("Enter your password: "), input("Hello, enter your email: "), int(input("Hello, enter your phone: "))))

