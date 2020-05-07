from db import *
from persona import *
from reporte import *
from so import *

class main():
	#constructor 
	def __init__(self):
		
		self.opcion = 0
		self.Logo = '''\n\n       		     ╔════════════════════════════╗ 
                     ║ SISTEMA DE HISORIA CLINICA ║ 
                     ╚════════════════════════════╝ '''

	#metodos 
	def DibujarLogo(self):
		print(self.Logo)
		
	def ValidaOpcion(self):
		print ('''	\n   |1 - ALTA PERSONA | '''+
	'''|2 - CONSULTAR PERSONAS| |3 - GENERAR REPORTE|  |4 - SALIR| \n''')

		try:
			self.opcion = int(input(' OPCION: '))
			
			if self.opcion == 1: # ALTA PERSONAS
				limpiarConsola()
				Principal.DibujarLogo()
				AltaPer(Dni, Ape, Nom)
				Principal.ValidaOpcion()
			if self.opcion == 2: # CONSULTA PERSONAS
				limpiarConsola()
				Principal.DibujarLogo()
				ConsultarPer()
				Principal.ValidaOpcion()
			if self.opcion == 3:	# GENERAR REPORTE
				limpiarConsola()
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
			ValidaOpcion()
Principal = main()
Principal.DibujarLogo()
Principal.ValidaOpcion()

