from typing import Deque
import urllib.request
import os
import requests
import numpy as np
import csv
import shutil
from matplotlib import pyplot as plt
import collections
from numpy import genfromtxt


def enfermos():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos") == False:
        os.mkdir('enfermos')
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    directorio = url.json()
    contador = 0
    for i in directorio:
        while contador < 4:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos" + "\\" + "enfermo" + str(contador) + ".csv") == False:
                urllib.request.urlretrieve(i ["download_url"] , "enfermo" + str(contador) + ".csv")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermo" + str(contador) + ".csv"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos"
                shutil.move(source, destination)
            contador += 1

def sanos():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos") == False:
        os.mkdir('sanos')
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    directorio = url.json()
    contador = 0
    for i in directorio:
        while contador < 4:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos" + "\\" + "sano" + str(contador) + ".csv") == False:
                urllib.request.urlretrieve(i ["download_url"] , "sano" + str(contador) + ".csv")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sano" + str(contador) + ".csv"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos"
                shutil.move(source, destination)
            contador += 1

class datoAgrupado:
    def __init__(self,numero,cantidad,fila):
        self.numero = numero
        self.cantidad = cantidad
        self.fila = fila

def compresor(matriz):
    cantidad = 0
    valor = 0
    promedio = 0
    iguales = False
    matrizComprimida = np.empty((0, 0), int)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):     
            if abs(matriz[i][j] - matriz[i][j+1]) < 15 and iguales == False:
                cantidad += 1
                valor = matriz[i][j]
                promedio = (matriz[i][j] + matriz[i][j+1])//2
                iguales = True
            elif abs(valor - matriz[i][j+1]) < 15 and iguales == True:
                cantidad += 1
            elif abs(valor - matriz[i][j+1]) > 15 and iguales == True:                
                matrizComprimida = np.append(matrizComprimida , datoAgrupado(promedio, cantidad, i) )                           
                cantidad = 0
                valor = 0
                promedio = 0
                iguales = False
            else:
                matrizComprimida = np.append(matrizComprimida , datoAgrupado(matriz[i][j], 1, i))                          
    return matrizComprimida

def main():
    enfermos()
    sanos()
    listaSanos = os.listdir("sanos")
    listaEnfermos = os.listdir("enfermos")
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos" + "\\" + "enfermo0.csv") as file_name:
        matriz = np.loadtxt(file_name, delimiter=",")
    #(matriz)
    #imgplot = plt.imshow(matriz)
    #plt.show()
    lista = compresor(matriz)
    contador = 0
    for i in range (len(lista)):
        contador +=1
        print("Numero: " + str(lista[i].numero) + " Cantidad: " + str(lista[i].cantidad) + " fila: " + str(lista[i].fila))
        #estos son los valores que se guardarian
    print(contador)#estos son todos los valores que se guardan
        
main()

