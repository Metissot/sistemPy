from db import *
from tkinter import *
from persona import *
from reporte import *
from so import *
class main():
	#constructor 
	def __init__(self):
		self.winp = Tk()
		self.winp.title('SISTEMA DE CONSULTAS DE INHABILITADOS')
		self.winp.geometry('800x600')
		#imagen de fondo
		self.Imagebg = PhotoImage(file='T148.gif')
		self.LblFondo = Label(self.winp, image = self.Imagebg, bd = 0)
		self.LblFondo.place(x = 0, y = 0)
		
		# CRAMOS BARRA DE MENU PRINCIPAL
		self.Bmenu = Menu(self.winp)
		
		# CREAMOS LOS MENU 
		self.mnuPersonas = Menu(self.Bmenu)
		self.mnuReportes = Menu(self.Bmenu)
		self.mnuSalir = Menu(self.Bmenu)
		
		
		#COMANDOS DE LOS MENUS
		
		#PERSONAS
		self.mnuPersonas.add_command(label='ALTA PERSONAS', command = self.abrirABMper)
		self.mnuPersonas.add_command(label='CONSULTAR PERSONAS')
		#REPORTES
		self.mnuReportes.add_command(label='GENERAR REPORTE')
		#SALIR 
		self.mnuSalir.add_command(label='Salir', command = self.Salir)
		
		#AGREGAMOS MENU A LA BARRA 
		self.Bmenu.add_cascade(label='PERSONAS', menu = self.mnuPersonas)
		self.Bmenu.add_cascade(label='REPORTES', menu = self.mnuReportes)
		self.Bmenu.add_cascade(label='SALIR', menu = self.mnuSalir)
		self.winp.config(menu = self.Bmenu)
		self.winp.config(background = '#00CCFF')
		
		self.winp.mainloop()
		
		#self.opcion = 0
		

	#metodos 
	def DibujarLogo(self):
		print(self.Logo)
	
	def abrirABMper(self):
		Nper = persona()
	
	def Salir(self):
		quit(self)
		
	def ValidaOpcion(self):
		
		
		'''
		try:
			self.opcion = int(input('  OPCION: '))
			
			if self.opcion == 1:# ALTA PERSONAS
				
				
				#Principal.DibujarLogo()
				
				# Meter datos
				##AP = input('	Ingrese Apellido: ')

				#NO = input('	Ingrese Nombre: ')
				
				#IDAR = input('	Ingrese Area: ')
				
	
				Principal.ValidaOpcion()
				
			if self.opcion == 2: # CONSULTA PERSONAS
				Sop.limpiarConsola()
				Principal.DibujarLogo()
				Nper.ConsultarPer()
				Principal.ValidaOpcion()
			if self.opcion == 3:	# GENERAR REPORTE
				Sop.limpiarConsola()
				Principal.DibujarLogo()
				generarReporte()
				AbrirPdf()
				Principal.ValidaOpcion()
			if self.opcion == 4: # ejecutar grafico
				quit()
			else: 
				Principal.ValidaOpcion()
		except ValueError:
			print(' formato de datos incorrecto ')
			Sop.limpiarConsola()
			Principal.DibujarLogo()
			Principal.ValidaOpcion()
'''
	
	
		# INSTANCIAMOS 
Principal = main()
#Sop = Os()
#Nper = persona()
#Sop.limpiarConsola()
#Principal.DibujarLogo()
#Principal.ValidaOpcion()

