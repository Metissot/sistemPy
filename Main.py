from db import *
from persona import *
from reporte import *
from so import *
class main():
	#constructor 
	def __init__(self):
		
		self.opcion = 0
		self.Logo = '''
 ╔════════════════════════════════════════════════════════════════════════════════╗ 
 ║                           SISTEMA DE CONSULTA                                  ║ 
 ║                              INHABILITADOS                                     ║  
 ║                                                                                ║
 ╚════════════════════════════════════════════════════════════════════════════════╝
 '''


	#metodos 
	def DibujarLogo(self):
		print(self.Logo)
		
	def ValidaOpcion(self):
		print ('''	\n   |1 - ALTA PERSONA | '''+
	'''|2 - CONSULTAR PERSONAS| |3 - GENERAR REPORTE|  |4 - SALIR| \n''')

		try:
			self.opcion = int(input(' OPCION: '))
			
			if self.opcion == 1: # ALTA PERSONAS
				
				Sop.limpiarConsola()
				Principal.DibujarLogo()
				
				# Meter datos
				DO = int(input('	Ingrese Documento: '))

				AP = input('	Ingrese Apellido: ')

				NO = input('	Ingrese Nombre: ')
				
				IDAR = input('	Ingrese Area: ')
				
				Nper.AltaPer(DO, AP, NO, IDAR)
				
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
			if self.opcion == 4: # SALIR
				quit()
			else: 
				Principal.ValidaOpcion()
		except ValueError:
			print(' formato de datos incorrecto ')
			Sop.limpiarConsola()
			Principal.DibujarLogo()
			Principal.ValidaOpcion()

Principal = main()
Sop = Os()
Nper = persona()
Sop.limpiarConsola()
Principal.DibujarLogo()
Principal.ValidaOpcion()

