import os

class Os:
	
	def limpiarConsola(self):
		
		if os.name == "nt":
			os.system("cls")
			os.system('mode con: cols=85 lines=25')
		elif os.name == "posix":
			os.system("clear")
			os.system('printf "\033[8;85;25t"')
		else:
			pass
