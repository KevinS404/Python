# Este programa simula el sorteo del Loto
# Autor:
# Fecha:
# Versión:

## Bloque Definiciones

#Importaciones
import random

#Definición de Funciones

# Función que escoge los números del sorteo de Loto aleatoriamente
# entre el 1 y el 45
# Entrada: Sin entrada
# Salida: Lista con 7 números
def escogerNumeros():
    ganadores = []
    opciones = list(range(1,46))
    i = 0
    while i <= 6:
        ganador = random.choice(opciones)
        ganadores.append(ganador)
        opciones.remove(ganador)
        i = i + 1
    return ganadores

# Función que compara si los numeros jugados por el usuario
# están entre los sorteados o no y calcula la cantidad de
# aciertos
# Entrada: 2 listas (Numeros jugados y numeros sorteados)
# Salida: 1 lista (Número de aciertos y lista con los números acertados)
def compararAciertos(escogidos,numerosUsuario):
    i = 0
    acumulador = 0
    ganadores = []
    while i < len(numerosUsuario):
        if int(numerosUsuario[i]) in escogidos:
            acumulador = acumulador + 1
            ganadores.append(numerosUsuario[i])
        else:
            acumulador = acumulador + 0
        i = i + 1
    return [acumulador,ganadores]

## Bloque Principal

#Entrada
listaInicial = input("Ingrese 6 números distintos entre 1 y 45 separados por coma: ")
listaInicial = listaInicial.split(",")

#Procesamiento
listaGanadores = escogerNumeros()

resultado = compararAciertos(listaGanadores,listaInicial)

#Salida
if resultado[0] >= 3:
    print ("Usted ganó con",resultado[0],"aciertos. Sus números ganadores son",resultado[1],".")
else:
    print ("Usted no ganó, pero tuvo",resultado[0],"aciertos.")

print ("Los numeros ganadores son",listaGanadores)
