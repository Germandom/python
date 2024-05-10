from pygame import mixer
class Reproductor:
    archivo= None

    def __init__(self,archivo):
        self.archivo=archivo
        mixer.init()
        mixer.music.load(archivo)
    
    def play(self):
        mixer.music.play()
        return "reproducioendo musica"
    def pause(self):
        mixer.music.pause()
        return "la musica se ha pausado"
    def stop(self):
        mixer.music.stop()
        return "la musica se detuvo"
    def volume(self, v):
        mixer.music.set_volume(v)
        return "definiendo volumen a {}".format(v)