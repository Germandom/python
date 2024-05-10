from tkinter import *
from tkinter import ttk
ventana=Tk()
frm=ttk.Frame(ventana,padding=10)
frm.grid()


ttk.Label(frm,text="hola mundo").grid(column=0,row=0)
ttk.Button(frm,text="Quit",command=ventana.destroy).grid(column=1,row=0)
ventana.mainloop()