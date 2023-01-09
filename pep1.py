n = int(input("ingrese la cantidad de palabras: "))
i = 0
maximo = 0
palabra = ''
while i < n:
    palabra = input('ingrese una palabra: ')
    j = 0
    nuevoMax = 0
    sumaPalabra = 0
    while j< len(palabra):
        caracter = palabra[j]
        #todas las condiciones para el puntaje de la palabra

        j = j +1
    nuevoMax = sumaPalabra
    if(maximo < nuevoMax):
        palabraMax = palabra
        maximo = nuevoMax
    i = i + 1
print(maximo)
