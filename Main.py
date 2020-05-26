from db import *
from tkinter import *
from persona import *
from reporte import *
from oficio import *
from so import *

class main():
	#constructor 
	def __init__(self):
		self.winp = Tk()
		self.winp.title('SISTEMA DE CONSULTAS DE INHABILITADOS')
		self.winp.geometry('800x600')
		self.winp.config(bg = '#0087FF')
        
		#imagen de fondo
		self.Imagebg = PhotoImage(file='T148.gif')
		self.LblFondo = Label(self.winp, image = self.Imagebg, bd = 0)
		self.LblFondo.place(x = 0, y = 0)
		
		# CRAMOS BARRA DE MENU PRINCIPAL
		self.Bmenu = Menu(self.winp)
		
		
		
		
        # CREAMOS LOS MENU 
		self.mnuReportes = Menu(self.Bmenu, tearoff=0)
		self.mnuReportes.config(bg = 'black')
		self.mnuPersonas = Menu(self.Bmenu, tearoff=0)

		self.mnuSalir = Menu(self.Bmenu, tearoff=0)
   
		self.mnuOficio = Menu(self.Bmenu, tearoff=0)
        
		#PERSONAS
		self.mnuPersonas.add_command(label='ALTA PERSONAS', command = self.abrirABMper)
		self.mnuPersonas.add_command(label='CONSULTAR INHABILITADO')
		
        #OFICIOS
		self.mnuOficio.add_command(label='Inhabilitar', command 
		
		
		= self.AbrirOficio)

        #REPORTES
		self.mnuReportes.add_command(label='GENERAR REPORTE')
		#SALIR 
		self.mnuSalir.add_command(label='Salir', command = self.Salir)
		
		#AGREGAMOS MENU A LA BARRA 
		self.Bmenu.add_cascade(label='PERSONAS', menu = self.mnuPersonas)
		self.Bmenu.add_cascade(label='OFICIOS', menu = self.mnuOficio)
		self.Bmenu.add_cascade(label='REPORTES', menu = self.mnuReportes)
		self.Bmenu.add_cascade(label='SALIR', menu = self.mnuSalir)
		self.winp.config(menu = self.Bmenu)
		
		self.winp.iconbitmap('01.ico')
		self.winp.resizable(0,0)
	
		self.winp.config(bg = 'black')
		
		#self.winp.attributes('-fullscreen',True)

		#self.winp.bind("<F11>", lambda event: self.winp.attributes("-fullscreen",
        #                            not self.winp.attributes("-fullscreen")))
		#self.winp.bind("<Escape>", lambda event: self.winp.attributes("-fullscreen", False))
		
		
		
		self.winp.mainloop()
		
		

	#metodos 
	
	def abrirABMper(self):
		Nper = persona()
		
	def AbrirOficio(self):
		ofi = oficio()
			
	def Salir(self):
		quit()
		
	
	
		# INSTANCIAMOS 
Principal = main()
#Sop = Os()
#Nper = persona()
#Sop.limpiarConsola()
#Principal.DibujarLogo()
#Principal.ValidaOpcion()

