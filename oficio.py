from db import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class oficio():
	def __init__(self):
		
		
		
		self.win = Tk()
		self.win.title('Alta de Oficios')
		self.win.geometry('640x350')
		self.win.config(padx = 0, pady = 0, bg = '', bd = 1)



		#Frame1 (contenedor)
		self.Lframe1 = LabelFrame(self.win, text='', pady = 5, padx = 150, bd = 2)
		self.Lframe1.grid(row = 0, column = 0)
		
		
		#Caja de texto Documento Persona
		self.LbDni_In = Label(self.Lframe1, text='DNI del Infractor: * ')
		self.LbDni_In.grid(row=1, column= 0)
		self.TxtDni_In = Entry(self.Lframe1)
		self.TxtDni_In.grid(row=1,column=1)
				
		#Caja de texto Persona
		self.TxtApe2 = Entry(self.Lframe1)
		self.TxtApe2.grid(row=2,column=1,)
		self.TxtNom2 = Entry(self.Lframe1)
		self.TxtNom2.grid(row=2,column=2,)
				
				
		#Boton 
		self.BtnGraba = ttk.Button(self.Lframe1, text='Buscar', command = self.VerifDNI)
		self.BtnGraba.grid(row = 1, column = 2, columnspan = 2, sticky = W + E)
		
		#label informacion 
		self.LbInfo = Label(self.Lframe1, text='')
		self.LbInfo.grid(row=4, column= 1) 




		#Frame2 (contenedor)
		self.Lframe = LabelFrame(self.win, text='Inhabilitar', pady = 20, padx = 25, bd = 3)
		self.Lframe.grid(row = 5, column= 0)
		

		#Caja de texto fecha_of
		self.LbFecha_of = Label(self.Lframe, text='Fecha oficio: * ')
		self.LbFecha_of.grid(row=1, column= 1)
		self.TxtFecha_of = Entry(self.Lframe, width= 30)
		self.TxtFecha_of.grid(row=1,column=2)
		
		#combo box Juzgado
		self.LbJuzg = Label(self.Lframe, text='Juzgado N°: * ')
		self.LbJuzg.grid(row=2, column= 1)
		self.CmboJuz = ttk.Combobox(self.Lframe, width= 27)
		self.CmboJuz["values"] = ["1", "2", "3"]
		self.CmboJuz.grid(row=2,column=2)
		
		#Caja de texto Numero Acta
		self.LbNActa = Label(self.Lframe, text='Numero de acta: * ')
		self.LbNActa.grid(row=3, column= 1)
		self.TxtNActa = Entry(self.Lframe, width= 30)
		self.TxtNActa.grid(row=3,column=2)
		
		#Caja de texto Numero Causa
		self.LbNCau = Label(self.Lframe, text='Numero de Causa: * ')
		self.LbNCau.grid(row=4, column= 1)
		self.TxtNCau = Entry(self.Lframe, width= 30)
		self.TxtNCau.grid(row=4,column=2)
		
		#Caja de texto Fecha Resolucion
		self.LbFech_Re = Label(self.Lframe, text='Fecha Resolucion: * ')
		self.LbFech_Re.grid(row=5, column= 1)
		self.TxtFech_Re = Entry(self.Lframe, width= 30)
		self.TxtFech_Re.grid(row=5,column=2)
		
		#Caja de texto Numero Resolucion
		self.LbN_Re = Label(self.Lframe, text='Numero Resolucion: * ')
		self.LbN_Re.grid(row=6, column= 1)
		self.TxtN_Re = Entry(self.Lframe, width= 30)
		self.TxtN_Re.grid(row=6,column=2)
		
		#Caja de texto Fecha inicio Inhabilitacion
		self.LbFech_IN = Label(self.Lframe, text='Fecha Inhabilitacion: * ')
		self.LbFech_IN.grid(row=7, column= 1)
		self.TxtFech_IN = Entry(self.Lframe, width= 30)
		self.TxtFech_IN.grid(row=7,column=2)
		
		#Caja de texto Fecha fecha final inhabilitacion
		self.LbFech_fin = Label(self.Lframe, text='Fecha fin Inhabilitacion: * ')
		self.LbFech_fin.grid(row=8, column= 1)
		self.TxtFech_fin = Entry(self.Lframe, width= 30)
		self.TxtFech_fin.grid(row=8,column=2)
		
		
		
		#Boton 
		self.BtnGraba = ttk.Button(self.Lframe, text='Inhabilitar', command = self.InHabilitarPorBoton)
		self.BtnGraba.grid(row = 9, column = 2, columnspan = 2, sticky = W + E)
		self.TxtDni_In.focus()



		self.win.resizable(0,0)
		self.win.mainloop()
		
		
		
		
		
		
		
		
		
		
		
	def VerifDNI(self):
	
		if self.TxtDni_In.get() == '':

			self.LbInfo.config(text= "Ingrese un DNI")
			
		else:
			self.QPer()

	


	def QPer(self):
		
		DNI = self.TxtDni_In.get() 
		cursor.execute("SELECT * FROM PERSONAS where DNI_PER = "+DNI)
		#print(cursor)
		rows_per = cursor.fetchall()# Recorremos el primer registro con el método fetchone, devuelve una tupla
		
		
		
		for rows_per in rows_per:
			#print(rows_per[1])
			
			self.TxtApe2.insert(0, rows_per[1])
			self.TxtNom2.insert(0,rows_per[2])
			
			self.TxtApe2.config(bg = '#4D7A74')
			self.TxtNom2.config(bg = '#4D7A74')
	
	
	
	
			
	def Inhabilitar(self, FechaOf, NJuz, Nacta, Ncau, FecheRe, Nre, Dni, FechaIn, FechaFinIn):
		
		
		self.FechaOf = FechaOf
		self.NJuz = NJuz
		self.Nacta = Nacta
		self.Ncau = Ncau
		self.FecheRe = FecheRe
		self.Nre = Nre
		self.Dni = Dni
		self.FechaIn = FechaIn
		self.FechaFinIn = FechaFinIn
			
		
		# CON MYSQL
			
		cursor.execute("insert into oficios (FECHA_ING_OF, JUZ_N_OF, N_ACTA_OF, N_CAUSA_OF, FECHA_RES_OF, N_RESOL_OF, DNI_PER_OF, FECHA_INHA_OF, FECHA_FIN_IN_OF) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)" , [self.FechaOf, self.NJuz, self.Nacta, self.Ncau, self.FecheRe, self.Nre, self.Dni, self.FechaIn, self.FechaFinIn])
		conexion.commit()# Guardamos los cambios haciendo un commit
		messagebox.showinfo("Genial", "SE INHABILITO CORRECTAMENTE")
		self.win.destroy()
			
			#conexion.close()
		
	def InHabilitarPorBoton(self):
		print (self.TxtFecha_of.get())
		self.Inhabilitar(self.TxtFecha_of.get(), self.CmboJuz.get(), self.TxtNActa.get(), self.TxtNCau.get(), self.TxtFech_Re.get(), self.TxtN_Re.get(), self.TxtDni_In.get(), self.TxtFech_IN.get(), self.TxtFech_fin.get())		
		
			



#ofi = oficio()

