def leer(nombre):
    archivo = open(nombre,"r")
    listaTexto = archivo.readlines()
    archivo.close
    return listaTexto

nombreArchivo = input("Ingrese el nombre del archivo junto con su extensión(.txt): ")
texto = leer(nombreArchivo)

i = 0
largo = 0
palabraMasLarga = ""

for i in range (len(texto)):
    if texto[i] != "\n":
        texto[i] = texto.split(" ")
        if len(texto[i]) > largo:
             largo = len(texto[i])
             palabraMasLarga = texto[i]
    i += 1

print(palabraMasLarga)

    
