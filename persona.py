from db import *
class persona():
	
	def __init__(self):
		self.Dni = 0
		self.Ape = ''
		self.Nom = ''
		self.Are = 0
		self.mensajePer = '	\n	ALTA DE PERSONAS \n'
		
	def AltaPer(self, DO, AP, NO, IDAR):
		
		self.Dni = DO
		self.Ape = AP
		self.Nom = NO
		self.Are = IDAR
				
		try:
			cursor.execute("INSERT INTO PERSONAS VALUES " \
			"(?, ?, ?, ?)", (self.Dni, self.Ape, self.Nom, self.Are))
		
		
			conexion.commit()# Guardamos los cambios haciendo un commit
			print('	\n Se grabo en la Base de datos correctamente	\n')
			conexion.close()
		
		except sqlite3.IntegrityError:
			print('\n ERROR: EL DNI DE LA PERSONA YA ESTA CARGADA EN LA BASE DE DATOS \n')
			
			
			
	def ConsultarPer(self):
		
		print("\n\n LISTA DE PERSONAS \n\n")

		conexion = sqlite3.connect('osep.s3db')
		cursor.execute("SELECT * FROM PERSONAS")
		#print(cursor)
		rows_per = cursor.fetchall()# Recorremos el primer registro con el método fetchone, devuelve una tupla
		print('   DNI  | APELLIDO  | NOMBRE   | AREA\n')
		for rows_per in rows_per:
			print(rows_per)
		conexion.close()

	#AltaPer(Dni, Ape, Nom)
	#ConsultarPer()
		


