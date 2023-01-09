#Este programa se encarga de determinar la distancia hamming entre 2 strings del
#mismo largo
#BLOQUE DE DEFINICIONES
#Primero que nada le pediremos al usuario que ingrese los dos strings que se
#evaluaran
palabra1 = input('ingrese la primera palabra que quiera comparar: ')
palabra2 = input('ingrese la segunda palabra que quiera comparar: ')
#Una vez se tengan los strings usaremos iteraciones para ir comparando letra por
#letra y almacenando la distancia hamming en una variable
i = 0
acumulador = 0
while i < len(palabra1):
#Si en la misma posicion hay letras iguales el acumulador se mantendra intacto
    if palabra1[i] == palabra2[i]:
        acumulador = acumulador 
        i = i + 1
#Por otro lado,si las letras fueran distintas el acumulador aumentara en uno
    else:
        acumulador = acumulador + 1
        i = i + 1

#Finalemnte le informaremos al usuario cual es la distancia hamming entre ambas
#palabras
print('la distancia hamming entre estas palabras es de',acumulador)
   


    

                 
