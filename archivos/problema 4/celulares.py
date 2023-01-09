#archivo de texto con las señales ya registradas
registradas = open("networks.txt", 'r')
#archivo con la potencia de las señales buscadas
señales = open('signal-strenght.txt','r')
verificados = open('conn-priority.txt','w')
#Hacemos una lista de los nombres registrados
lista1 = registradas.readlines()
#Hacemos una lista de las señales disponibles
lista2 = señales.readlines()
#Esta lista es para guardar los nombres de las señales disponibles
listaNombres =[]
#Esta lista es para guardar las intensidades de los nombres de la lista anterior
listaIntensidades =[]
#Lista para copiar la lista 1 pero sacando los caracteres que nos molestan
listaRegistrados = []

for elemento in lista2:
    #de la lista2 hacemos una mini lista de cada uno de sus elementos
    #separandolos por ','
    miniLista = elemento.split(',')
    #Sabemos que el primer elemento de esta lista es el nombre, asi que lo
    #agregamos a la lista de nombres
    listaNombres.append(miniLista[0])
    #Con estas 3 variables sacamos los caracteres que acompañan al numero
    #en la segunda posicion de la lista
    sacar1 = '\n'
    sacar2 = '-'
    sacar3 = ''
    nuevo = miniLista[1]
    nuevo = nuevo.replace(sacar1,"")
    nuevo = nuevo.replace(sacar2,"")
    nuevo = nuevo.replace(sacar3,"")
    #una vez "limpio" el string, vemos si efectivamente es un numero
    if(nuevo.isnumeric()):
        #Convertimos el string a numero y lo pasamos a la lista de intensidades
        entero = int(nuevo)
        listaIntensidades.append(entero)
#Con este ciclo limpiamos la lista1 y la traspasamos a la lista de registrados
for elemento1 in lista1:
    nuevo1 = elemento1
    nuevo1 = nuevo1.replace(sacar1,"")
    nuevo1 = nuevo1.replace(sacar3,"")
    listaRegistrados.append(nuevo1)

listaConexiones = []
listaI = []
#ahora se analiza la lista de registrados para comparar con la que tiene
#las señales disponibles
for registrado in listaRegistrados:
    for disponible in listaNombres:
        if(registrado == disponible):
            listaConexiones.append(disponible)
            intensidad = listaNombres.index(disponible)
            ayura = listaIntensidades[intensidad]
            listaI.append(ayura)
        

listaCopia = listaI[:]
for i in range(len(listaI)):
    for j in range(i+1,len(listaI)):
        if listaI[i] > listaI[j]:
            listaI[i],listaI[j] =listaI[j],listaI[i]

stringArchivo = ''
i = 1
while(len(listaCopia)!= 0):
    for elemento in listaCopia:
        verificador = listaI[0]
        if verificador == elemento:
            indice = listaCopia.index(elemento)
            aux = str(elemento)
            aux2 = str(i)
            stringArchivo += aux2 +','+listaConexiones[indice]+',-'+aux+'\n'
            i +=1
            listaCopia.pop(indice)
            listaConexiones.pop(indice)
            listaI.pop(0)
      
print(stringArchivo)    
verificados.write(stringArchivo)
registradas.close()
señales.close()
verificados.close()
