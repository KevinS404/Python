#Este programa determina si un numero es palindromo o no
#ENTRADA: un numero (int)
#SALIDA: un mensaje (string)
#Le pedimos el numero al usuario
n = (input('ingrese un numero entero positivo: '))
#Ahora haremos de este numero una lista
lista = list(n)
#Guardaremos una copia
listaCopia = lista[:]
#Aqui buscamos invertir la lista

#Hacemos una lista vacia que servira para comprobar si el numero es o no palindromo
listaInvertida =[]
#De esta manera nos aseguramos de ir agregando el ultimo elemento de la lista
#copiada a la lista invertida
while len(lista) != 0:
    variable = lista.pop()
    listaInvertida.append(variable)


#Una vez invertida la lista,comprobamos que sea igual a la original
#Si las listas son iguales,el numero capicua
if listaCopia == listaInvertida:
    print('el numero capicua')

#Si no son iguales,no capicua
else:
    print('el numero no capicua')


    
