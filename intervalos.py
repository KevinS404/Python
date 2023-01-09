#Este programa se encarga de encontrar donde se encuentra un numero en intervalos
#ya dados
#ENTRADAS: numero a evaluar
#SALIDAS: intervalo al que pertenece el numero
numero = float(input('ingrese el numero que quiere evaluar: '))
#Ahora establecemos los intervalos
if numero >= 4 and numero <= 6:
    print('el valor que usted ingreso se encuentra entre 4 y 6')
elif numero >= 3 and numero <= 7:
    print('el valor que usted ingreso se encuentra entre 3 y 7')
elif numero >= 2 and numero <= 8:
    print('el valor que usted ingreso se encuentra entre 2 y 8')
elif numero >= 1 and numero <= 9:
    print('el valor que usted ingreso se encuentra entre 1 y 9')
elif numero < 0:
    print('el valor es menor que 0')
elif numero >= 10:
    print('el valor es mayor o igual a 10')

               
