def sumaCubos(x,y):
    suma = x**3 + y**3
    return suma
def listaCubos(numero):
    listaDeCubos = []
    i = 1
    while i <= numero:
        j = 1
        while j <= numero:
            if sumaCubos(i,j) <= numero:
                if not [i,j] in listaDeCubos and not [j,i] in listaDeCubos:
                    listaDeCubos.append([i,j])
            j = j + 1
        i = i + 1
                
    return listaDeCubos

def igualdadCubos(lista):
    listaDeSumas = []
    i = 0
    while i < len(lista):
        suma = sumaCubos(lista[i][0],lista[i][1])
        listaDeSumas.append(suma)
        i = i + 1
    return listaDeSumas

def cumplenCondicion(numero):
    lista_cubos = listaCubos(numero)
    lista_suma = igualdadCubos(lista_cubos)
    lista_condicion = []
    largo = len(lista_cubos)
    i = 0
    arbitro = False
    while i < largo:
        j = i + 1
        while j < largo:
            if lista_suma[i] == lista_suma[j]:
                lista_condicion.append([lista_cubos[i],lista_cubos[j]])
            j = j + 1
        i = i + 1
    return lista_condicion
            
                
                
        

#Entrada
numero = int(input("Ingrese numero: "))

#Proceso
cubosValidos = cumplenCondicion(numero)

#salida
print("Los numeros que cumplen la condicion son: ")
for sublista in cubosValidos:
    a = sublista[0][0]
    b = sublista[0][1]
    c = sublista[1][0]
    d = sublista[1][1]
    print("{0}³ + {1}³ = {2}³ + {3}³ ≤ {4}".format(a,b,c,d,numero))
    
