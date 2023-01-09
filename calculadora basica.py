#Este programa cumple la funcion de una calculadora basica
#ENTRADAS: 2 numeros y la operacion que se realizara
#SALIDAS: el numero resultante de la operacion
#Le pedimos los numeros a los usuarios
numero1 = float(input('ingrese el primero numero: '))
numero2 = float(input('ingrese el segundo numero: '))
#Ahora le solicitaremos la operacion
operacion = input('ingrese la operacion que desea: ')
#Ahora hacemos que el programa decida
if operacion == 'suma':
    resultado = numero1 + numero2
if operacion == 'resta':
    resultado = numero1 - numero2
if operacion == 'multiplicacion':
    resultado = numero1 * numero2
if operacion == 'division':
    resultado = numero1 / numero2

print('el resultado es', resultado)
