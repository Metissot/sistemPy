from db import *
from persona import *
from reporte import *
from so import *


# ----- VARIABLES
opcion = 0
Logo = '''\n\n       		     ╔════════════════════════════╗ 
                     ║ SISTEMA DE HISORIA CLINICA ║ 
                     ╚════════════════════════════╝ '''

#--------------------- FIN VARIABLES
print(Logo)

#AltaPer(Dni, Ape, Nom)
#ConsultarPer()
def ValidaOpcion():
	print ('''	\n   |1 - ALTA PERSONA | '''+
'''|2 - CONSULTAR PERSONAS| |3 - GENERAR REPORTE|  |4 - SALIR| \n''')

	try:
		opcion = int(input(' OPCION: '))
		
		if opcion == 1: # ALTA PERSONAS
			limpiarConsola()
			print(Logo)
			AltaPer(Dni, Ape, Nom)
			ValidaOpcion()
		if opcion == 2: # CONSULTA PERSONAS
			limpiarConsola()
			print(Logo)
			ConsultarPer()
			ValidaOpcion()
		if opcion == 3:	# GENERAR REPORTE
			limpiarConsola()
			print(Logo)
			generarReporte()
			AbrirPdf()
			ValidaOpcion()
		if opcion == 4: # SALIR
			quit()
		else: 
			ValidaOpcion()
	except ValueError:
		
		print(' formato de datos incorrecto ')
		ValidaOpcion()
ValidaOpcion()

