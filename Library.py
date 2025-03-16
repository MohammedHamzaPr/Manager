from tkinter import *
from tkinter import ttk
import sqlite3 as mysql
from tkinter import messagebox
from datetime import datetime
from threading import Thread
from os import getcwd
try:
    connect = mysql.connect('data.db',check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data(id TEXT, name TEXT, age TEXT, job TEXT, email TEXT, gender TEXT, address TEXT, Fc TEXT, recruitment TEXT, pn TEXT) ')
except:
    messagebox.showerror('Server','Please Turn On Server MySQL')
    exit()
