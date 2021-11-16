from typing import Deque
import urllib.request
import os
import requests
import numpy as np
import csv
import cv2
import shutil
from PIL import Image
from matplotlib import pyplot as plt
from collections import deque
from numpy import genfromtxt
import sys
import time



def enfermos():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos") == False:
        os.mkdir('enfermos')
    urlEnfermos =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    directorio = urlEnfermos.json()
    contador = 0
    for i in directorio:
        if contador < 3:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos" + "\\" + "enfermo" + str(contador) + ".csv") == False:
                urllib.request.urlretrieve(i ["download_url"] , "enfermo" + str(contador) + ".csv")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermo" + str(contador) + ".csv"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermos"
                shutil.move(source, destination)
            contador += 1

def sanos():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos") == False:
        os.mkdir('sanos')
    urlSanos =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    directorio = urlSanos.json()
    contador = 0
    for i in directorio:
        if contador < 3:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos" + "\\" + "sano" + str(contador) + ".csv") == False:
                urllib.request.urlretrieve(i ["download_url"] , "sano" + str(contador) + ".csv")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sano" + str(contador) + ".csv"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanos"
                shutil.move(source, destination)
            contador += 1

def enfermosImagenes():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenes") == False:
        os.mkdir('enfermosImagenes')
    urlEnfermosImagenes =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/gris/enfermo_gris')
    directorio = urlEnfermosImagenes.json()
    contador = 0
    for i in directorio:
        if contador < 2:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenes" + "\\" + "enfermo" + str(contador) + ".jpg") == False:
                urllib.request.urlretrieve(i ["download_url"] , "enfermo" + str(contador) + ".jpg")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermo" + str(contador) + ".jpg"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenes"
                shutil.move(source, destination)
            contador += 1

def sanosImagenes():
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenes") == False:
        os.mkdir('sanosImagenes')
    urlSanosImagenes =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/gris/sano_gris')
    directorio = urlSanosImagenes.json()
    contador = 0
    for i in directorio:
        if contador < 2:
            if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenes" + "\\" + "sano" + str(contador) + ".jpg") == False:
                urllib.request.urlretrieve(i ["download_url"] , "sano" + str(contador) + ".jpg")
                source = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sano" + str(contador) + ".jpg"
                destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenes"
                shutil.move(source, destination)
            contador += 1

def guardarSanosComprimidos(nombreImagen):
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesComprimidas") == False:
        os.mkdir('sanosImagenesComprimidas')
    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesComprimidas" + "\\" + nombreImagen) == False:
        source = os.path.dirname(os.path.abspath(__file__)) + "\\" + nombreImagen
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesComprimidas"
        shutil.move(source, destination)

def guardarSanosDescomprimidos(nombreImagen):
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesDescomprimidas") == False:
        os.mkdir('sanosImagenesDescomprimidas')
    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesDescomprimidas" + "\\" + nombreImagen) == False:
        source = os.path.dirname(os.path.abspath(__file__)) + "\\" + nombreImagen
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "sanosImagenesDescomprimidas"
        shutil.move(source, destination)

def guardarEnfermosComprimidos(nombreImagen):
    if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenesComprimidas") == False:
        os.mkdir('enfermosImagenesComprimidas')
    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenesComprimidas" + "\\" + nombreImagen) == False:
        source = os.path.dirname(os.path.abspath(__file__)) + "\\" + nombreImagen
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\" + "enfermosImagenesComprimidas"
        shutil.move(source, destination)

def cargarElArchivo(nombre):
    with open(nombre) as archivo:
        texto = archivo.read()
        return texto
    
def sacarFilasYColumnas(texto):
    filas = texto.split("\n")
    fila0 = filas[0].split(",")
    return len(filas), len(fila0)

def crearMatriz(texto,numeroDeFilas,numeroDeColumnas):
    matriz = np.zeros( (numeroDeFilas,numeroDeColumnas) )
    filas = texto.split("\n")
    i = 0
    for fila in filas:
        j = 0 
        columnas = fila.split(",")
        for columna in columnas:
            if columna != '':
                matriz[i][j] = int(columna)
                j = j + 1
        i = i + 1
    return matriz


def substring(sub1, sub2):
    maxLongest = 0
    offset = 0
    for i in range(0, len(sub1)):
        longest = 0
        if ((i == len(sub1) - len(sub2) - 2)):
            break
        for j in range(0, len(sub2)):
            if (i+j < len(sub1)):
                if sub1[i+j] == sub2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset


def compresionConPerdidas(img):
    #print('Dimensiones originales: ',img.shape)
    scale_percent = 30 # a que porcentaje se reduce
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # mermar tamaño
    imagenComprimida = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('ComprimidaConPerdidas.jpg',imagenComprimida) #guardar imagen
    #print('Dimensiones nueva imagen: ',imagenComprimida.shape)
    #solo es para mostrar la imagen esto de abajo
    #cv2.imshow("nueva imagen", resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print("Tamano imagen original: " + str(sys.getsizeof(img)))
    #print("Tamano imagen comprimida con perdidas: " + str(sys.getsizeof(imagenComprimida)))
    return imagenComprimida


def compresionSinPerdidas (text):
    searchWindowSize = 20
    previewWindowSize = 20
    encodedNumbers = []
    encodedSizes = []
    encodedLetters = []
    i = 0
    while i < len(text):
        if i < previewWindowSize:
            encodedNumbers.append(0)
            encodedSizes.append(0)
            encodedLetters.append(text[i])
            i = i + 1
        else:
            previewString = text[i:i+previewWindowSize]
            searchWindowOffset = 0
            if (i < searchWindowSize):
                searchWindowOffset = i
            else:
                searchWindowOffset = searchWindowSize
            searchString = text[i - searchWindowOffset:i]
            result = substring(searchString + previewString, previewString) # searchString + prevString, prevString
            nextLetter = ''
            if (result[0] == len(previewString)):
                if (i + result[0] == len(text)):
                    nextLetter = ''
                else:
                    nextLetter = text[i+previewWindowSize]
            else:
                nextLetter = previewString[result[0]]
            if (result[0] == 0):
                encodedNumbers.append(0)
                encodedSizes.append(0)
                encodedLetters.append(nextLetter)
            else:
                encodedNumbers.append(searchWindowOffset - result[1])
                encodedSizes.append(result[0])
                encodedLetters.append(nextLetter)
            i = i + result[0] + 1
    return encodedNumbers, encodedSizes, encodedLetters


def descompimirConPerdidas(img):
    #print('Dimensiones originales: ',img.shape)
    porcentajeDeEscalado = 350 # a que porcentaje se aumenta
    width = int(img.shape[1] * porcentajeDeEscalado / 100)
    height = int(img.shape[0] * porcentajeDeEscalado / 100)
    dim = (width, height)
    # mermar tamaño
    imagenDescomprimida = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('DescomprimidaConPerdidas.jpg',imagenDescomprimida) #guardar imagen
    #print('Dimensiones nueva imagen: ',imagenDescomprimida.shape)
    #cv2.imshow("nueva imagen", resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print("Tamano imagen comprimida con perdidas: " + str(sys.getsizeof(img)))
    #print("Tamano imagen descomprimida con perdidas: " + str(sys.getsizeof(imagenDescomprimida)))
    return imagenDescomprimida


def desCompresionSinPerdidas (encodedNumbers, encodedSizes, encodedLetters):    
    i = 0
    decodedString = []
    while i < len(encodedNumbers):
        if (encodedNumbers[i] == 0):
            decodedString.append(encodedLetters[i])
        else:
            currentSize = len(decodedString)
            for j in range(0, encodedSizes[i]):
                decodedString.append(decodedString[currentSize-encodedNumbers[i]+j])
            decodedString.append(encodedLetters[i])
        i = i+1
    return decodedString


def compresionConPerdidas2(nombreArchivo):
    print(nombreArchivo[0])
    if nombreArchivo[0] == "s":
        img = cv2.imread("sanosImagenes\\" + nombreArchivo)
    else:
        img = cv2.imread("enfermosImagenes\\" + nombreArchivo)
    #print('Dimensiones originales: ',img.shape)
    scale_percent = 30 # a que porcentaje se reduce
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # mermar tamaño
    imagenComprimida = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    nombre = nombreArchivo + "comprimidaConPerdidas.jpg"
    cv2.imwrite(nombre,imagenComprimida) #guardar imagen
    #print('Dimensiones nueva imagen: ',imagenComprimida.shape)
    #solo es para mostrar la imagen esto de abajo
    #cv2.imshow("nueva imagen", resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print("Tamano imagen original: " + str(sys.getsizeof(img)))
    #print("Tamano imagen comprimida con perdidas: " + str(sys.getsizeof(imagenComprimida)))
    return nombre

def descompimirConPerdidas2(nombreArchivo):
    if nombreArchivo[0] == "s":
        img = cv2.imread("sanosImagenesComprimidas\\" + nombreArchivo)
    else:
        img = cv2.imread("enfermosImagenesComprimidas\\" + nombreArchivo)
    #print('Dimensiones originales: ',img.shape)
    porcentajeDeEscalado = 350 # a que porcentaje se aumenta
    width = int(img.shape[1] * porcentajeDeEscalado / 100)
    height = int(img.shape[0] * porcentajeDeEscalado / 100)
    dim = (width, height)
    # mermar tamaño
    imagenDescomprimida = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    nombre = nombreArchivo + "descomprimidaConPerdidas.jpg"
    cv2.imwrite(nombre,imagenDescomprimida) #guardar imagen
    #print('Dimensiones nueva imagen: ',imagenDescomprimida.shape)
    #cv2.imshow("nueva imagen", resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print("Tamano imagen comprimida con perdidas: " + str(sys.getsizeof(img)))
    #print("Tamano imagen descomprimida con perdidas: " + str(sys.getsizeof(imagenDescomprimida)))
    return nombre


def grabarEnUnArchivoCSV(nombre, matriz):
    filas, columnas = matriz.shape
    with open(nombre,'w') as archivo:
        for i in range(filas):
            for j in range(columnas):
                archivo.write(str(matriz[i][j]))
                archivo.write(",")
            archivo.write("\n")

def main():
    #enfermos()
    #sanos()
    enfermosImagenes()
    sanosImagenes()
    listaSanos = os.listdir("sanosImagenes")
    listaEnfermos = os.listdir("enfermosImagenes")
    
    # compresion con perdidas
    for i in range (len(listaSanos)):
        archivo = cv2.imread("sanosImagenes\\" + listaSanos[i])
        #print(listaSanos[i])
        imgLossComp = compresionConPerdidas(archivo)
        imgLossDescomp = descompimirConPerdidas(imgLossComp)
        
    for i in range (len(listaEnfermos)):
        archivo = cv2.imread("enfermosImagenes\\" + listaEnfermos[i])
        #print(listaEnfermos[i])
        imgLossComp = compresionConPerdidas(archivo)
        imgLosslessDescomp = descompimirConPerdidas(imgLossComp)
        
        
    # compresion sin perdidas
    for i in range (len(listaSanos)):
        archivoImagen = cv2.imread("enfermosImagenes\\" + listaEnfermos[i])
        archivo = (listaSanos[i])
        my_string = np.asarray(Image.open("sanosImagenes\\" + archivo),np.uint8)        
        stringToEncode = str(my_string.tolist())            
        [a,b,c] = compresionSinPerdidas(stringToEncode)
        imgLossDescomp = desCompresionSinPerdidas(a,b,c)
    
    for i in range (len(listaEnfermos)):
        archivo = (listaEnfermos[i])
        my_string = np.asarray(Image.open("enfermosImagenes\\" + archivo),np.uint8)        
        stringToEncode = str(my_string.tolist())            
        [a,b,c] = compresionSinPerdidas(stringToEncode)
        imgLosslessDescomp = desCompresionSinPerdidas(a,b,c)
    
main()