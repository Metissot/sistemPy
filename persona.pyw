
from db import *

Dni = 0
Ape = ''
Nom = ''
mensajePer = '	\n	ALTA DE PERSONAS \n'
mensajePer2 = '¡este campo no puede estar vacio!' 



	
def AltaPer(Dni, Ape, Nom):
	print(mensajePer)
	
	Dni = int(input('	Ingrese Documento: '))

	Ape = input('	Ingrese Apellido: ')

	Nom = input('	Ingrese Nombre: ')
	
	try:
		
		cursor.execute("INSERT INTO PERSONAS VALUES " \
		"(?, ?, ?, ?)", (Dni, Ape, Nom, ''))
	
	
		conexion.commit()# Guardamos los cambios haciendo un commit
		print('	\n Se grabo en la Base de datos correctamente	\n')
		conexion.close()
	
	except sqlite3.IntegrityError:
		print('\n ERROR: EL DNI DE LA PERSONA YA ESTA CARGADA EN LA BASE DE DATOS \n')
		AltaPer(Dni, Ape, Nom)
		
		
def ConsultarPer():
	
	print("\n\n LISTA DE PERSONAS \n\n")

	conexion = sqlite3.connect('osep.s3db')
	cursor.execute("SELECT * FROM PERSONAS")
	#print(cursor)
	rows_per = cursor.fetchall()# Recorremos el primer registro con el método fetchone, devuelve una tupla
	for rows_per in rows_per:
		print(rows_per)
	conexion.close()

#AltaPer(Dni, Ape, Nom)
#ConsultarPer()
	


