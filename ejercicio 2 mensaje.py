"""
Este programa descifra mensajes codificados
Autores: Kevin Silva(20.495.193-4)
version: 1.8
ENTRADAS: palabras (lista)
SALIDA: mensaje (string)
"""
#Le solicitamos al usuario que ingrese un mensaje
palabras= input('ingrese el mensaje: ').split()
#PROCESAMIENTO
#En una variable guardamos el largo de la lista de palabras
largoDeMensaje = len(palabras)
#Creamos 2 variables vacias para poder iterar y crear el mensaje
mensajeDescifrado = ''
caracterOculto = ''
i = 0
#iteramos mientras i sea menor que el largo de la lista
while i < largoDeMensaje:
    #hacemos una lista de cada palabra de la lista grande
    listaPalabra = list(palabras[i])
    #Ahora iteramos cada letra de la palabra   
    j=0
    #Esta condicion se da si la palabra fuera mas pequeña que el largo del mensaje  
    if len(listaPalabra)<largoDeMensaje+1:
        #Esto se ejecutara mientras la condicion de arriba se cumpla
        while len(listaPalabra)<largoDeMensaje+1:
            #Para esto se hace una copia de la lista,y se agrega a la misma
            #para poder hacer una busqueda de manera circular y que se pueda
            #ejecutar la condicion de mas abajo
            listaCopia = listaPalabra[:]
            listaPalabra += listaCopia
        
   #Esta condicion se da en caso de que el largo de la palabra sea mas grande que
   #el largo del mensaje
    if len(listaPalabra)>=largoDeMensaje+1:
        #Esto se ejecutara mientras la condicion de arriba se cumpla
        while j < largoDeMensaje+1:
            #en esta variable vamos almacenando la letra que estamos buscando
            #de cada palabra
            caracterOculto = listaPalabra[j]
            j = j + 1
    #Esta variable es la que ira almacenando el mensaje final
    mensajeDescifrado = mensajeDescifrado + caracterOculto
               

    i = i + 1

        

#Le entregamos al usuario el mensaje descifrado
print('el mensaje descifrado es:',mensajeDescifrado)

