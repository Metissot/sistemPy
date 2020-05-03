from tkinter import *

var = StringVar()

#def ConsultarUser():
    
 #   UserTemp = TxtBox.get()
   
   # if UserTemp == "mauri":
  #      msg='correcto'
  #  else:
   #     msg='incorrecto'
   # return var.set(msg)   
           
# VENTANA PRINCIPAL

Vent = Tk()
Vent.title('Probando TKINTER')
Vent.geometry("640x480")

# CAMPO DE TEXTO USER

Label(Vent, text='USUARIO').grid(row=1,  column=1)
TxtBox = Entry(Vent)
TxtBox.grid(row=1, column=2)

# CAMPO DE TEXTO CLAVE

Label(Vent, text='CLAVE').grid(row=1, column=6)
TxtBox2 = Entry(Vent)
TxtBox2.grid(row=1, column=7)

# BOTON

boton = Button(Vent, text="prees", command=ConsultarUser).place(x=300, y=400)
 

Vent.mainloop()

    
