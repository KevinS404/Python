#Este programa se encarga de simular el videojuego BUSCAMINAS
#debera pedir un ancho, alto y una probabilidad determinada
#Importamos random desde el modulo random
from random import random

#Esta funcion se encarga de genera la matriz a partir de las entradas del usuario
#Entradas: el valor del ancho(fila) y alto(columna) de la matriz
#Salida: matriz de FilaxColumna
def crearMatriz(fila, columna):
    #Creamos una lista vacia para la matriz
    matriz = []
    #Para cada espacio en el rango del ancho,agregamos una S
    for i in range(fila):
        #Esto lo multiplicamos por el valor del alto para genera la matriz
        matriz.append(['S']*columna)
    return matriz

#Esta funcion se encarga de generar el campo en base a la probabilidad que ingresa
#el usuario
#Entrada: probabilidad del usuario
#Salida: existencia de minas en el campo
def campoAsignado(probabilidad):
    #Se genera una probabilidad entre 0 y 1 
    numero = random()
    #Esta variable guarda un valor booleano para poder comparar
    existeMina = False
    #Si la probabilidad que ingresa el usuario es de 1, si o si habra una mina
    if probabilidad == 1:
        existeMina = True
    #Por el otro lado,si la probabilidad es de 0 no habra mina
    elif probabilidad == 0:
        existeMina = False
    #Si la probabilidad es mayor que el numero generado aleatoriamente,habra una
    #mina
    elif probabilidad > numero:
        existeMina = True
    return existeMina

#Esta funcion se encarga de generar las minas en el campo
#Entrada: la matriz generada
#Salida: cantidad de minas
def generaMinas(matrizInicial):
    for i in range(len(matrizInicial)):
        for j in range(len(matrizInicial[0])):
            if campoAsignado(probabilidad):
                matrizInicial[i][j] = 'B'       
    return matrizInicial
#Esta funcion escribe el campo minado en el archivo de salida
#Entrada: archivo en modo de agregacion
#Salida: archivo con el campo minado
def escribirCampoMinado(campoMinado):
    for elemento in matrizFinal:
        string = ''
        for letra in elemento:
            string += str(letra)
        campoMinado.write(string + '\n')
    campoMinado.close()
    return campoMinado

    
    
          
#Entradas    
fila = int(input('ingrese el ancho del campo: '))
columna = int(input('ingrese el alto del campo: '))
probabilidad = float(input('ingrese la probabilidad entre 0 y 1: '))

campoMinado = open('Campo Minado.txt','a')

#Procesamiento
matrizInicial = crearMatriz(fila, columna)
matrizFinal = generaMinas(matrizInicial)
#Salidas
campo = escribirCampoMinado(campoMinado)





