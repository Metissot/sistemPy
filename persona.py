from db import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
class persona():
		
	def __init__(self):
		
		
		self.win = Tk()
		self.win.title('ABM PERSONAS')
		self.win.geometry('480x350')
		self.win.config(pady = 50 , padx = 80)
		
		#creamos un frame (contenedor)
		self.Lframe = LabelFrame(self.win, text='Alta Personas', pady = 5, padx = 5, bd = 1)
		self.Lframe.grid(row = 0, column = 3)
		
		#Caja de texto Documento
		self.LblDoc = Label(self.Lframe, text='Documento: * ')
		self.LblDoc.grid(row=1, column= 1)
		self.TxtDoc = Entry(self.Lframe)
		self.TxtDoc.grid(row=1,column=2)
		
		# caja de texto Apellido 
		self.LblApe = Label(self.Lframe, text='Apellido: * ')
		self.LblApe.grid(row=3, column= 1)
		self.TxtApe = Entry(self.Lframe)
		self.TxtApe.grid(row=3,column=2)
		
		# caja de texto Nombre 
		self.LblNom = Label(self.Lframe, text='Nombre: * ')
		self.LblNom.grid(row=5, column= 1)
		self.TxtNom = Entry(self.Lframe)
		self.TxtNom.grid(row=5,column=2)
		
		# caja de texto lICENCIA 
		self.LblAre = Label(self.Lframe, text='N Licencia de Conducir :  ')
		self.LblAre.grid(row=7, column= 1)
		self.TxtAre = Entry(self.Lframe)
		self.TxtAre.grid(row=7,column=2)
		
		# caja de domicilio  
		self.LblDom = Label(self.Lframe, text='Domicilio :  ')
		self.LblDom.grid(row=8, column= 1)
		self.TxtDom = Entry(self.Lframe)
		self.TxtDom.grid(row=8,column=2)
		
		# caja de contacto  
		self.LblCon = Label(self.Lframe, text='Contacto :  ')
		self.LblCon.grid(row=9, column= 1)
		self.TxtCon = Entry(self.Lframe)
		self.TxtCon.grid(row=9,column=2)
		
		#creamos Boton
		self.BtnGraba = ttk.Button(self.Lframe, text='Grabar', command = self.VerifTxt)
		self.BtnGraba.grid(row = 10, column = 2, columnspan = 2, sticky = W + E)
		
		self.LblInfo = Label(self.Lframe, text='')
		self.LblInfo.grid(row=11, column= 2)
		
		
		self.TxtDoc.focus()
		
		#self.win.config(background = '#58ACFA')
		self.win.resizable(0,0)
		self.win.mainloop()
		
		self.Dni = self.TxtDoc.get()
		self.Ape = self.TxtApe.get()
		self.Nom = self.TxtNom.get()
		self.Are = self.TxtAre.get()
		
	def CrearVent(self):
		pass
		
		
		
	def VerifTxt(self):
		self.LblInfo.config(text= "")
		
		if self.TxtDoc.get() == '':
			#messagebox.showinfo("Atencion", "Debe ingresar un DNI")
			self.LblInfo.config(text= "Debe ingresar un DNI")
			self.TxtDoc.focus()
		elif self.TxtApe.get() == '':	
			#messagebox.showinfo("Atencion", "Debe ingresar un Apellido")
			self.LblInfo.config(text= "Debe ingresar Apellido")
			
		elif self.TxtNom.get() == '':	
			#messagebox.showinfo("Atencion", "Debe ingresar un Nombre") 
			self.LblInfo.config(text= "Debe ingresar nombre")
		else :
			self.AltaPer()
		
		
		
	def AltaPer(self):
		
		self.Dni = self.TxtDoc.get()
		self.Ape = self.TxtApe.get()
		self.Nom = self.TxtNom.get()
		self.Are = self.TxtAre.get()
		#CON SQLITE				
		#cursor.execute("INSERT INTO personas VALUES " \
		#"(?, ?, ?, ?)", (self.Dni, self.Ape, self.Nom, self.Are))
		
		# CON MYSQL
		try:
			
			cursor.execute("insert into personas (DNI_PER, APE_PER, NOM_PER, N_LICPER) values (%s, %s, %s, %s)" , [self.Dni,self.Ape,self.Nom,self.Are])
			conexion.commit()# Guardamos los cambios haciendo un commit
			self.LblInfo.config(text= "DATOS GRABADOS")
			self.DesTxt()
			#conexion.close()
			#self.win.destroy()
		except mysql.connector.errors.IntegrityError:
			#messagebox.showinfo("Atencion", "EL DNI DE LA PERSONA YA ESTA CARGADA EN LA BASE DE DATOS")
			self.LblInfo.config(text= "LA PERSONACON ESE DNI YA TIENE UN REGISTRO EN LA BASE DE DATOS")
			
	def DesTxt(self):
		self.TxtDoc.config(state=DISABLED)		
			
			
	def ConsultarPer(self):
		
		

		#conexion = sqlite3.connect('osep.s3db')
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
#self.ConsultaPer()
