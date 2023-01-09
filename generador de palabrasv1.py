'''
Este programa se encarga de genera tantas palabras como el usuario quiera y del
tamaño que desee
autor:Kevin Silva(20.495.193-4)
'''
#Primero importamos la funcion choice del modulo random
from random import choice
#Le pedimos al usuario la cantidad de palabras que quiere,asi como su largo
n = int(input('ingrese la cantidad de palabras que desea: '))
m = int(input('ingrese el tamaño de las palabras: '))
#Necesitamos las letras del alfabeto,pero hacemos una lista solo de vocales
#y de consonantes
vocales = ['a','e','i','o','u']
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
consonantes =['b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z']
#PROCESAMIENTO
#Hacemos una lista para guardar las futuras palabras
palabras = []
#Hacemos una condicion en caso de que el usuario ingrese un numero <= 0
if n <= 0 or m <= 0:
    print('con estos datos el programa no puede funcionar')
#Usando las entradas del usuario, haremos uso de iteraciones
i = 0
#La condicion se ejecutara hasta que se tengan todas las palabras deseadas
while i < n:
    j = 0
    #Creamos un string vacio para la palabra en esta posicion que cuando se
    #agregue la palabra a la lista,esta variable se vuelva a "vaciar"
    palabra = ''
    #la condicion se ejecutara hasta que se tenga el largo pedido 
    while j < m:
        #Ahora tomamos en cuenta las condiciones
        #Nos aseguramos de que cada palabra comienze por una vocal
        if palabra == '':
            palabra += choice(vocales)
            j = j + 1
        
        else:
            #Si la ultima letra agregada fue una vocal,podemos agregar cualquier
            #letra en el alfabeto
            if palabra[-1] in vocales:
                palabra += choice(alfabeto)
                j = j + 1
            #Si la ultima letra agregada fue una consonante,agregaremos una vocal    
            elif palabra[-1] in consonantes:
                palabra += choice(vocales)
                j = j + 1
    #Una vez lista la palabra la agregamos a la lista de palabras
    palabras.append(palabra)
    i = i + 1

#Devolvemos los iteradores a 0 para volver a usarlos
i = 0
#Una vez generada las palabras, se procede a sacarles la puntuacion
#Hacemos una lista vacia para las puntuaciones
puntuaciones = []
#Esto lo hacemos de manera de poder separar la lista del alfabeto por secciones
seccion1 = int(alfabeto.index('g'))+1
seccion2 = int(alfabeto.index('o'))+1
#La seccion final se puede sacar a partir de las 2 anteriores
while i < len(palabras):
    j = 0
    #Hacemos una lista de cada palabra para poder iterarla
    verificador = list(palabras[i])
    #Generamos una variable para la puntuacion de cada palabra
    puntuacion = 0
    while j < len(palabras[i]):
        #Si la letra se encuentra entre a y g
        if verificador[j] in alfabeto[:seccion1]:
            puntuacion = puntuacion + 1
        #Si la letra se encuentra entre h y o
        elif verificador[j] in alfabeto[seccion1:seccion2]:
            puntuacion = puntuacion + 2
        #Si la letra se encuentra entre p y z    
        elif verificador[j] in alfabeto[seccion2:]:
            puntuacion = puntuacion + 3
        j = j + 1
    #Agregamos la puntuacion a la lista
    puntuaciones.append(puntuacion)
    #Devolvemos la variable a su estado inicial
    puntuacion = 0
    i = i  + 1
#Ahora mediante iteracion imprimimos los datos que se nos pidieron
k = 0
while k < len(palabras):
    print(palabras[k],puntuaciones[k],'puntos')
    k = k + 1
        
        
    
    

               
    

                
            
                
        
        


