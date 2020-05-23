from tkinter import *

#var = StringVar()

#def ConsultarUser():
    
 #   UserTemp = TxtBox.get()
   
   # if UserTemp == "mauri":
  #      msg='correcto'
  #  else:
   #     msg='incorrecto'
   # return var.set(msg)   
           
# VENTANA PRINCIPAL
def fun():
	

	
	TxtBox2.insert(1, (1,2))



Vent = Tk()
Vent.title('Probando TKINTER')
Vent.geometry("640x480")

# CAMPO DE TEXTO USER

Label(Vent, text='USUARIO').grid(row=0,  column=0)
TxtBox = Entry(Vent)
TxtBox.grid(row=0, column=1)

# CAMPO DE TEXTO CLAVE

Label(Vent, text='CLAVE').grid(row=1, column=0)
TxtBox2 = Entry(Vent)
TxtBox2.grid(row=1, column=1)

# BOTON

boton = Button(Vent, text="prees", command=fun )
boton.grid(row = 3, column = 2)
 

Vent.mainloop()

