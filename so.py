import os

def limpiarConsola():
	
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")
	else:
		pass
