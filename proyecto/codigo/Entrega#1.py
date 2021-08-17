import urllib.request
import os
from os import remove
import requests



def Cargar ():
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    directorio = url.json()
    contador = 0
    
    lista = []
    for i in directorio:
        urllib.request.urlretrieve(i ["download_url"] , "vaca" + str(contador) + ".csv")   
        
        with open("vaca" + str(contador) + ".csv" , "r") as archivo: 
            
            csv = archivo.read()
            
            lista.append(csv)
            print (lista)
            archivo.close()
            remove(os.path.dirname(os.path.realpath("Entrega#1 final")) + "\\" + archivo.name)
            lista.clear()       # borramos el contenido de la lista para hacer más dinámico el proceso, sin embargo, sabemos que esto no se debe hacer en la entrega final porque se perderían los datos anteriores
            contador += 1    
    return lista

def _main_ ():
    Cargar()         

_main_()