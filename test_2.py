from urllib import request
from urllib.error import URLError

mp=["puta","mierda", "pelotudo", "macaco","culio", "bobo"]

def ver_contenido(url):
    try:
        f=request.urlopen(url)
    except URLError:
        return ('la URL'+ url +'no esxiste')
    else:
        contenido= f.read()
        aux=contenido.split()
        palabras_encontradas=[]
        cant_mp=0
        for m in mp:
            for con in aux:
                if m in con.decode():
                    palabras_encontradas.append(m)
                    cant_mp=cant_mp+1
                    
        return palabras_encontradas        
                    
            
        

url='https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("\n---------------------------------------------------------------")
print("informe del sitio: ")
print(ver_contenido(url))

    