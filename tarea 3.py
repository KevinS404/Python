#Este programa se encarga de hacer una busqueda preeliminar para la tiena Alterna
#Music para filtrar sus discos
#Esta funcion separa los discos del archivo con su respectiva informacion y los
#deja en una lista aparte
def ordenarDiscos(discos):
    listaDiscos = []
    for linea in discos:
        linea = linea.strip()
        listaDiscos.append(linea)
    return listaDiscos
#Se abre el archivo y se almacena la lista en una variable
discos = open('DISCOS.txt','r')
listaDeDiscos = ordenarDiscos(discos)
#Le pediremos al usuario que ingrese los filtros que quiere
fecha1 = int(input('Ingrese año inicial: '))
fecha2 = int(input('Ingrese año final: ' ))
genero = input('Ingrese el genero que prefiere: ').lower()
print('Popularidad disponible desde 0 hasta 10')
popularidad = float(input('Ingrese desde que numero desea ver la popularidad: '))
precio1 = int(input('Ingrese la cantidad minima de dinero: '))
precio2= int(input('Ingrese la cantidad maxima de dinero: '))
print('¿Desea buscar a una banda en especifico?')
verificador = input('Responder si o no: ')
if verificador == 'si':
    verificador = True
    banda = input('Ingrese el nombre de la banda: ')
else:
    verificador = False
    banda = ''
#Esta lista almacena los discos que serviran finalmente
listaFinal = []
#Si el usuario no busca un nombre especifico se ejecuta esto
if verificador == False:
    #Ahora usaremos la lista para abrir cada archivo con la informacion del disco
    #y poder filtrarla con lo que quiere el usuario
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        #Estas variables verifican si el disco cumple con los requisitos
        #y en cada ciclo vuelven a su valor inicial
        rating = False
        fecha = False
        precio = False
        clasificacion = False
        for linea in informacionDisco:
            linea = linea.strip()
            #Si la linea fuera un numero vemos los filtros que sean numeros
            if linea.isdigit():
                if int(linea)>= fecha1 and int(linea)<= fecha2:
                    fecha = True
                elif int(linea) >= precio1 and int(linea) <= precio2:
                    precio = True
            #Esto se ejecuta si la linea es texto o es la linea que almacena
            #la popularidad
            else:
                if linea[1] == '.' or linea[2] == '.':
                    if float(linea) >= popularidad and float(linea) <= 10:
                        rating = True
                if linea.lower() == genero:
                    clasificacion = True
           #Si se cumple que todas son verdad,el disco nos sirve
            if rating == fecha == precio == clasificacion == True:
                listaFinal.append(disco)
                rating = False
                fecha = False
                precio = False
                clasificacion = False
#Si el usuario quiere algo en especifico se ejecuta esto
if verificador == True:
    #hacemos el mismo proceso del primer caso pero con una variable mas
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        rating = False
        fecha = False
        precio = False
        clasificacion = False
        #Esta es la unica variable distinta de la sentencia anterior
        nombre = False
        for linea in informacionDisco:
            linea = linea.strip()
            #Si la linea fuera un numero vemos los filtros que sean numeros
            if linea.isdigit():
                if int(linea)>= fecha1 and int(linea)<= fecha2:
                    fecha = True
                elif int(linea) >= precio1 and int(linea) <= precio2:
                    precio = True    
            else:
                if linea.lower() == banda:
                    nombre = True
                elif linea[1] == '.' or linea[2] == '.':
                    if float(linea) >= popularidad and float(linea) <= 10:
                        rating = True
                elif linea.lower() == genero:
                    clasificacion = True
           #Si se cumple que todas son verdad,el disco nos sirve
            if rating == fecha == precio == clasificacion == nombre == True:
                listaFinal.append(disco)
                rating = False
                fecha = False
                precio = False
                clasificacion = False
                nombre = False
if len(listaFinal) > 0:
    print('El o los discos que a usted le pueden interesar son:')
    for elemento in listaFinal:
        print(elemento)
else:
    print('No se ha encontrado un disco con esas caracteristicas.')
    
        



                          


                    
            
                    
                    
                
                
                
            
            
            
            
            
                
            
 
    

    
   
            
            
