from db import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
class persona():
		
	def __init__(self):
		
		
		self.win = Tk()
		self.win.title('ABM PERSONAS')
		self.win.geometry('480x240')
		
		#creamos un frame (contenedor)
		self.Lframe = LabelFrame(self.win, text='Alta Personas' )
		self.Lframe.grid(row = 0, column = 0, columnspan = 10, pady = 20)
		
		#Caja de texto Documento
		self.LblDoc = Label(self.Lframe, text='  Documento: ')
		self.LblDoc.grid(row=1, column= 1)
		self.TxtDoc = Entry(self.Lframe)
		self.TxtDoc.grid(row=1,column=2)
		
		# caja de texto Apellido 
		self.LblApe = Label(self.Lframe, text='Ingrese Apellido: ')
		self.LblApe.grid(row=2, column= 1)
		self.TxtApe = Entry(self.Lframe)
		self.TxtApe.grid(row=2,column=2)
		
		# caja de texto Nombre 
		self.LblNom = Label(self.Lframe, text='Ingrese Nombre: ')
		self.LblNom.grid(row=3, column= 1)
		self.TxtNom = Entry(self.Lframe)
		self.TxtNom.grid(row=3,column=2)
		
		# caja de texto Area 
		self.LblAre = Label(self.Lframe, text='Ingrese Area: ')
		self.LblAre.grid(row=4, column= 1)
		self.TxtAre = Entry(self.Lframe)
		self.TxtAre.grid(row=4,column=2)
		
		#creamos Boton
		self.BtnGraba = ttk.Button(self.Lframe, text='Grabar', command = self.VerifTxt)
		self.BtnGraba.grid(row = 5, column = 2, columnspan = 2, sticky = W + E)
		
		self.LblInfo = Label(self.Lframe, text='')
		self.LblInfo.grid(row=1, column= 1)
		
		
		self.TxtDoc.focus()
		
		#self.win.config(background = '#58ACFA')
		self.win.mainloop()
		
		self.Dni = self.TxtDoc.get()
		self.Ape = self.TxtApe.get()
		self.Nom = self.TxtNom.get()
		self.Are = self.TxtAre.get()
		
	def CrearVent(self):
		pass
		
		
		
	def VerifTxt(self):
		
		
		if self.TxtDoc.get() == '':
			messagebox.showinfo("Atencion", "Debe ingresar un DNI")
			self.TxtDoc.focus()
		elif self.TxtApe.get() == '':	
			messagebox.showinfo("Atencion", "Debe ingresar un Apellido")
			
		elif self.TxtNom.get() == '':	
			messagebox.showinfo("Atencion", "Debe ingresar un Nombre") 
		else :
			self.AltaPer()
		
	def AltaPer(self):
		
		self.Dni = self.TxtDoc.get()
		self.Ape = self.TxtApe.get()
		self.Nom = self.TxtNom.get()
		self.Are = self.TxtAre.get()
						
		try:
			cursor.execute("INSERT INTO PERSONAS VALUES " \
			"(?, ?, ?, ?)", (self.Dni, self.Ape, self.Nom, self.Are))
		
		
			conexion.commit()# Guardamos los cambios haciendo un commit
			messagebox.showinfo("Atencion", "DATOS GRABADOS")
			conexion.close()
			quit()
		except sqlite3.IntegrityError:
			messagebox.showinfo("Atencion", "EL DNI DE LA PERSONA YA ESTA CARGADA EN LA BASE DE DATOS")
			
			
			
			
	def ConsultarPer(self):
		
		

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
		

#per = persona()
#per.AltaPer()
