#Este programa simula el escape de Stroud
#ENTRADA:lista del recorrido
#SALIDA: el tiempo utilizado y el que sobre
print('Cada letra representa lo siguiente')
print('S = stroud')
print('C = camino libre')
print('G = camino con guardia')
print('L = llave')
print('S = salida')
print('recuerde que Stroud tiene que estar necesariamente de los primeros')
print('y todos los caracteres tienen que estar en mayuscula!')
recorrido = input('Ingrese los caracteres mencionados separados por espacio: ').split()
tiempo = int(input('Ingrese el tiempo disponible en horas para el escape: '))
#Hacemos una copia de este tiempo
tiempoCopia = tiempo
#Hacemos una variable para la llave
llave = ''
#Tenemos que tener en consideracion el tiempo,mientras haya podremos seguir
#haciendo que Stroud se mueva
#Este caso es cuando la persona ingresa un valor positivo
i = 1
if tiempo > 0:
    #Esto al igual que la llave lo hacemos para tener constancia de si se encontro
    #cada una de ellas
    salida = ''
    #Ahora iteramos
    while i < len(recorrido) or llave == '' or salida == '':
        if recorrido[i] == 'C':
            tiempo = tiempo - 1
            #Esto es por si tenemos que retroceder en algun momento
            recorrido[i] = 'c'
        elif recorrido[i] == 'G':
            tiempo = tiempo - 2
            recorrido[i] = 'g'
        elif recorrido[i] == 'L':
            tiempo = tiempo - 1
            llave = 'obtenida'
            recorrido[i] = 'l'
        elif recorrido[i] == 'S':
            salida = 'encontrada'
            tiempo = tiempo - 1
            recorrido[i]= 's'

        if salida == 'encontrada' and llave == 'obtenida':
            i = len(recorrido)
    
        i = i + 1

if i > len(recorrido):
    if 'C' in recorrido:
        recorrido.remove('C')
    if 'G' in recorrido:
        recorrido.remove('G')
    i = len(recorrido)

print(recorrido)

#Esto pasa si llegamos al final de la lista
if i == len(recorrido):  
    #Podemos invertir la lista para devolvernos
    recorridoInverso = recorrido[::-1]
    j = 1
    print(recorridoInverso)
    if recorridoInverso[j] == 's' and llave == 'obtenida':
        tiempo = tiempo - 0.5
    else:
        while j < len(recorridoInverso):
            if recorridoInverso == 'c':
                tiempo = tiempo - 0.5
            elif recorridoInverso[j] == 'g':
                tiempo = tiempo - 1
            elif recorridoInverso[j] == 's':
                tiempo = tiempo - 0.5
                j = len(recorridoInverso)
            j = j + 1
print('tiempo de sobra',tiempo,'horas')                  
tiempoEscape = tiempoCopia - tiempo
print('le tomo escapar',tiempoEscape,'horas')

        
        
    
        
    
    
        
    



            
            
        


