#import sqlite3

import mysql 
import mysql.connector as mariadb
from tkinter import messagebox

# CON SQLITE
#conexion = sqlite3.connect('db.s3db')
#cursor = conexion.cursor()

try:

	def conectar():
		conexion = mariadb.connect(host='localhost', port='3306',
									   user='root', password='', database='muni')

	def CerrarCon():
		conexion.close()
except mysql.connector.errors.InterfaceError:
	messagebox.showinfo("Atencion", "NO SE PUDO CONECTAR CON LA BASE DE DATOS O NO EXISTE")
	pass
