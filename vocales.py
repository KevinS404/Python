#Programa que determina el numero de vocales existentes en un oracion

#BLOQUE DE DEFINICIONES

#Le pediremos al usuario que nos entrege la oracion que quiere analizar y haremos
#una copia de la misma
oracion = input('Ingrese la oracion que desee: ')
oracionCopia = oracion
#Ahora para no complicarnos con mayusculas o minusculas haremos que todo sea minuscula
oracion = oracion.lower()
#Aqui estableceremos un string que guarde las vocales para poder evaluar mas tarde
vocales = 'aeiou'
#Ahora con iteraciones recorreremos los strings para evaluarlos y guardaremos la cantidad
#en un acumulador
acumulador = 0
i = 0
while i < len(oracion):
    j = 0
    while j < len(vocales):
        if oracion[i] == vocales[j]:
            acumulador = acumulador + 1
        j = j + 1
    i = i + 1

#Salidas
#Aqui entregaremos la oracion que el usuario nos dio y la cantidad de vocales que posee

        
print('La oracion que usted entrego es:')
print(oracionCopia)
print('Y la cantidad de vocales que contiene es:')
print(acumulador)
