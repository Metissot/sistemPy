from db import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
class persona():
		
	def __init__(self):
		
		
		self.win = Tk()
		self.win.title('ABM PERSONAS')
		self.win.geometry('480x350')
		self.win.config(bg = '#303030')
		
		fondo = '#303030'
		txtFondo = 'grey'
		Col_let = 'snow'
		TxtPadx = 5
		TxtPady = 5
		
		#creamos un frame (contenedor)
		self.Lframe = LabelFrame(self.win, text='Alta Personas', bd = 1, bg = fondo, fg = Col_let)
		self.Lframe.grid(row = 0, column = 3, pady = 15, padx = 30)
		
		#Caja de texto Documento
		self.LblDoc = Label(self.Lframe, text='Documento: * ', bg = fondo, fg = Col_let)
		self.LblDoc.grid(row=1, column= 1, padx = 10, sticky = "w")
		self.TxtDoc = Entry(self.Lframe,width= 40, bg = txtFondo, fg = Col_let)
		self.TxtDoc.grid(row=1,column=2, pady = 10, padx = 10 , sticky = "w")
		
		# caja de texto Apellido 
		self.LblApe = Label(self.Lframe, text='Apellido: * ', bg = fondo, fg = Col_let)
		self.LblApe.grid(row=3, column= 1, padx = 10, sticky = "w")
		self.TxtApe = Entry(self.Lframe, width= 40, bg = txtFondo, fg = Col_let)
		self.TxtApe.grid(row=3,column=2, pady = 10, padx = 10, sticky = "w")
		
		# caja de texto Nombre 
		self.LblNom = Label(self.Lframe, text='Nombre: * ', bg = fondo, fg = Col_let)
		self.LblNom.grid(row=5, column= 1, padx = 10, sticky = "w")
		self.TxtNom = Entry(self.Lframe, width= 40, bg = txtFondo, fg = Col_let)
		self.TxtNom.grid(row=5,column=2, pady = 10, padx = 10, sticky = "w")
		
		# caja de texto lICENCIA 
		self.LblAre = Label(self.Lframe, text='N Licencia de Conducir :  ', bg = fondo, fg = Col_let)
		self.LblAre.grid(row=7, column= 1, padx = 10, sticky = "w")
		self.TxtAre = Entry(self.Lframe, width= 40, bg = txtFondo, fg = Col_let)
		self.TxtAre.grid(row=7,column=2, pady = 10, padx = 10, sticky = "w")
		
		# caja de domicilio  
		self.LblDom = Label(self.Lframe, text='Domicilio :  ', bg = fondo, fg = Col_let)
		self.LblDom.grid(row=8, column= 1, padx = 10, sticky = "w")
		self.TxtDom = Entry(self.Lframe, width= 40, bg = txtFondo, fg = Col_let)
		self.TxtDom.grid(row=8,column=2, pady = 10, padx = 10, sticky = "w")
		
		# caja de contacto  
		self.LblCon = Label(self.Lframe, text='Contacto :  ', bg = fondo, fg = Col_let)
		self.LblCon.grid(row=9, column= 1, padx = 10, sticky = "w")
		self.TxtCon = Entry(self.Lframe, width= 40, bg = txtFondo, fg = Col_let)
		self.TxtCon.grid(row=9,column=2, pady = 10, padx = 10, sticky = "w")
		
		#creamos Boton
		self.BtnGraba = ttk.Button(self.Lframe, text='Grabar', command = self.VerifTxt)
		self.BtnGraba.grid(row = 10, column = 1, columnspan = 2, sticky = W + E, pady = 15)
		
		self.LblInfo = Label(self.Lframe, text='', fg = 'red', bg = fondo)
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
