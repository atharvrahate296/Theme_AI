import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from Main import main_screen
from Main import signup_page

# after authentication write the data to sqlite file
def write_data(uname,s_email,s_password):
    # write signup data to file
    connect = sqlite3.connect("user_registry.sqlite")
    cursor = connect.cursor()

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Login_details (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime varchar(255),
        name varchar(255),
        email varchar(255),
        password varchar(255)
    )
    ''')
    connect.commit()

    cursor.execute('''
    SELECT email FROM Login_details WHERE email = ?
    ''', (s_email,))
    result = cursor.fetchone()

    if result:
        messagebox.showwarning(title="Signup Error", message="User already exists!  logging you in.")
    else:
        cursor.execute('''
        INSERT INTO Login_details (datetime, name, email, password)
        VALUES (?, ?, ?, ?)
        ''', (current_time, uname, s_email, s_password))
        connect.commit()

    connect.close()
    main_screen(name=uname)

def confirm_account(l_email,l_password):
    # check if the user exists in database using email
    connect = sqlite3.connect("user_registry.sqlite")
    cursor = connect.cursor()

    cursor.execute('''
        SELECT name, password FROM Login_details WHERE email = ?
    ''', (l_email,))
    global result
    result = cursor.fetchone()
    
    connect.close()
    if result:
        name, password = result
        if l_password == password:
            return True,name
        else:
            return 2
    else:
        return False

