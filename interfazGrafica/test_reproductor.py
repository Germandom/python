from tkinter import *
from tkinter.ttk import *
from Reproductor import *

musica = Reproductor('wefere.mp3')

def play_musica():
    musica.volume(0.8)
    musica.play

master=Tk()
master.geometry("200x200")

label= Label(master,text="Reproductor de musica")
 
label.pack(pady=10)

btn_play=Button(master,text="reproducir", command=play_musica)
btn_play.pack(pady=10)

mainloop()