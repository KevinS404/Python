#Este programa se encarga de mostrarle a Hanamichi cuantas veces supero su
#maximo y cuantas empeoro su minimo
#ENTRADA: puntuaciones (lista)
#SALIDA: texto (string)

#BLOQUE PRINCIPAL
#Le pediremos que ingrese la lista con las puntuaciones
lista = (input('ingrese los puntos de esta temporada separados: ')).split()
#lista = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
#Ahora haremos una funcion que ordene la lista guardando cada vez que se supere
#o que empeore
i = 0
print(lista)
minimo = int(lista[i])
maximo = int(lista[i])
acumuladorMaximo = 0
acumuladorMinimo = 0
while i < len(lista):
    if int(lista[i]) > int(maximo):
        maximo = lista[i]
        acumuladorMaximo += 1
        
    if int(lista[i]) < int(minimo):
        minimo = lista[i]
        acumuladorMinimo += 1
        
    
    i = i + 1
    
        
    
    
print(acumuladorMaximo)
print(acumuladorMinimo)


            
        


        
            



