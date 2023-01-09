#Este programa se encarga de redondear un numero a cierta cantidad de decimales
#que el usuario quiera
#Le pedimos el numero al usuario
numero = input('ingrese el numero que quiere evaluar:')
#Hacemos de este numero una lista
listaDecimal = numero.split(".")
#Tambien necesitamos la cantidad de decimales que quiere
n = int(input('ingrese la cantidad de decimas que quiere ver: '))
#Ahora dividimos este numero en 2 partes
parteEntera = listaDecimal[0]
parteDecimal = listaDecimal[1]
print(parteDecimal)
#Ahora con la cantidad de decimales que ingreso el usuario verificamos la lista






