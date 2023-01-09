#Este programa se encarga de mostrar el camino que se realiza en la conjetura de collatz

numero = int(input('ingrese un numero entero: '))

while numero != 1:
    if numero % 2 == 0:
        numero = numero / 2
        print(numero)

    else:
        numero = (numero*3) + 1
        print(numero)
