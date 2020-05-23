#import sqlite3

import mysql 
import mysql.connector as mariadb
from tkinter import messagebox

# CON SQLITE
#conexion = sqlite3.connect('db.s3db')

conexion = mariadb.connect(host='localhost', port='3306',
									   user='root', password='', database='muni')

cursor = conexion.cursor()
