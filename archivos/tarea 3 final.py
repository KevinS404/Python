#Este programa se encarga de hacer una busqueda preeliminar para la tiena Alterna
#Music para filtrar sus discos
#AUTOR: Kevin silva (20.495.193-4)
#BLOQUE DE DEFINICIONES
#Esta funcion separa los discos del archivo con su respectiva informacion y los
#deja en una lista aparte
def ordenarDiscos(discos):
    listaDiscos = []
    for linea in discos:
        linea = linea.strip()
        listaDiscos.append(linea)
    return listaDiscos
#BLOQUE PRINCIPAL
#Se abre el archivo y se almacena la lista en una variable
discos = open('DISCOS.txt','r')
listaDeDiscos = ordenarDiscos(discos)
#Ahora se ve que filtro quiere el usuario
print('De las siguientes opciones: ')
print('1- Filtrar por fechas de lanzamiento(años).')
print('2- Filtrar por genero musical.')
print('3- Filtrar por popularidad(maximo 10).')
print('4- Filtrar por dentro de un rango de precios.')
print('5- Elegir una banda o artista especifico.')
#Se almacena la respuesta del usuario
respuesta = input('Eliga el numero de la opcion que usted prefiera: ')
#Se hace una lista para almacenar los discos que serviran finalmente
listaFinal = []
#PROCESAMIENTO
#Ahora se decide segun la respuesta del usuario
if respuesta == '1':
    fecha1 =int(input('ingrese el año mas antiguo que desea buscar: '))
    fecha2 = int(input('ingrese el año mas reciente que desea buscar hasta la fecha: '))
    #Usamos la lista de discos para abrir cada archivo que contiene la informacion
    #de cada uno de los discos
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        #Este valor se encarga de registrar si el disco esta dentro del rango
        fecha = False
        for linea in informacionDisco:
            linea = linea.strip()
            if linea.isdigit():
                if int(linea) >= fecha1 and int(linea) <= fecha2:
                    fecha = True
            if fecha == True:
                #Si el valor de fecha coincide en el rango del usuario
                #agregamos el disco y devolvemos fecha a su valor inicial
                listaFinal.append(disco)
                fecha = False
if respuesta == '2':
    preferencia = input('ingrese el genero que prefiere: ').lower()
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r') 
        #Este valor se encarga de registrar si el disco cumple con el filtro
        genero = False
        for linea in informacionDisco:
            linea = linea.strip()
            if isinstance(linea,str):
                if linea.lower() == preferencia:
                    genero = True
                if genero == True:
                    listaFinal.append(disco)
                    genero = False
if respuesta == '3':
    popularidad = float(input('ingrese desde que numero desea ver la popularidad: '))
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        rating = False
        listaInformacion = informacionDisco.readlines()
        if float(listaInformacion[3]) >= popularidad :
            rating = True
        if rating == True:
            listaFinal.append(disco)
            rating = False
if respuesta == '4':
    precio1 = int(input('ingrese la cantidad minima de dinero: '))
    precio2 = int(input('ingrese la cantidad maxima de dinero que le interesa: '))
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        precio = False
        listaInformacion = informacionDisco.readlines()
        if int(listaInformacion[4]) >= precio1 and int(listaInformacion[4])<= precio2:
            precio = True
        if precio == True:
            listaFinal.append(disco)
            precio = False
      
if respuesta == '5':
    banda = input('ingrese el nombre de la banda o artista: ').lower()
    for disco in listaDeDiscos:
        informacionDisco = open(disco +'.txt','r')
        nombre = False
        for linea in informacionDisco:
            linea = linea.strip()
            if linea.lower() == banda:
                nombre = True
            if nombre == True:
                listaFinal.append(disco)
                nombre = False

#Nos aseguramos de cerrar todo
discos.close()
informacionDisco.close()
#Si se encontraron discos que cumplen los requisitos, se lo informamos al usuario
if len(listaFinal) > 0:
    print('Los discos que le podrian interesar son:')
    for elemento in listaFinal:
        print(elemento)
#Si no hubiera ningun disco con las caracteristicas buscadas se lo informamos
if len(listaFinal) == 0:
    print('No se ha podido encontrar algun disco con esas caracteristicas.')
    
        
                

            
    
    
    


        
    
    

        



                          


                    
            
                    
                    
                
                
                
            
            
            
            
            
                
            
 
    

    
   
            
            
