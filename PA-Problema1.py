#Este programa se encarga de determinar que numero es "perfecto" a partir de sus
#divisiones enteras

#Esta funcion se encarga de obtener los divisores para cada numero
#Entrada: el numero del usuario
#Salida: retorna la lista con los divisores
def obtenerDivisores(numero):
    #Hacemos una lista para los divisores
    listaDivisores = []
    #para cada numero en el rango de 1 hasta el numero-1, vemos si la division
    #da resto 0
    for i in range(1,numero):
        if numero%i==0:
            #En caso de funcionar,agregamos ese numero a la lista
            listaDivisores.append(i)
    #retornamos la lista
    return listaDivisores

#Esta funcion se encarga de determinar si el numero es perfecto o no
#Entrada: el numero del usuario
#Salida: retorna un valor booleano 
def esPerfecto(numero):
    #Llamamos a la funcion anterior
    divisores = obtenerDivisores(numero)
    #Sumamos todos sus dividores
    sumaDivisores = sum(divisores)
    #Si el numero es perfecto,retornamos un valor True
    if sumaDivisores == numero:
        return True
    else:
        return False
    
#Esta funcion se encarga de determinar la cantidad de numeros perfectos que
#solicito el usuario
#Entrada: el numero del usuario
#Salida: la lista con los numeros perfectos   
def cantidadDePerfectos(numero):
    #ListaPara la cantidad de perfectos
    cantidad = []
    i = 1
    #Mientras la cantidad de perfectos sea distinta del numero, determinamos si
    #el numero es perfecto llamando a la funcion anterior y agregando el numero
    #que corresponda
    while len(cantidad) != numero:
        if esPerfecto(i):
            cantidad.append(i)
        i = i + 1
    #retornamos la cantidad
    return cantidad
    
#ENTRADA
numero = int(input("ingrese un numero: "))

#PROCESO
numerosPerfectos = cantidadDePerfectos(numero)

#SALIDA
print(numerosPerfectos)
    
    
