#Este programa se encarga de hacer una busqueda preeliminar para la tienda Alterna
#Music para filtrar sus discos
#AUTOR: Kevin silva (20.495.193-4)
#BLOQUE DE DEFINICIONES
#Esta funcion separa los discos del archivo con su respectiva informacion y los
#deja en una lista
def ordenarDiscos(discos):
    listaDiscos = []
    for linea in discos:
        linea = linea.strip()
        listaDiscos.append(linea)
    return listaDiscos
#Esta funcion se encarga de filtrar los discos a partir de lo que ingrese
#el usuario y retorna una lista con los discos de interes
def filtrarDiscos(listaDeDiscos,respuesta):
    #Se hace una lista para almacenar los discos que serviran finalmente
    listaFinal = []
    #Ahora se decide segun la respuesta del usuario
    if respuesta == '1':
        fecha1 =int(input('Ingrese el año mas antiguo que desea buscar: '))
        fecha2 = int(input('Ingrese el año mas reciente que desea buscar hasta la fecha: '))
        #Usamos la lista de discos para abrir cada archivo que contiene la 
        # imformacion de cada uno de los discos
        for disco in listaDeDiscos:
            informacionDisco = open(disco +'.txt','r')
            #Este valor se encarga de registrar si el disco esta dentro del rango
            fecha = False
            #Hacemos una lista temporal de los datos de cada disco
            listaInformacion = informacionDisco.readlines()
            if float(listaInformacion[1])>= fecha1 and float(listaInformacion[1])<=fecha2:
                fecha = True
            if fecha == True:
                #Si la fecha coincide con el rango que ingreso el usuario
                #agregamos el disco a la lista
                listaFinal.append(disco)
                fecha = False
        
    if respuesta == '2':
        preferencia = input('Ingrese el genero que prefiere: ').lower()
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
        popularidad = float(input('Ingrese desde que numero desea ver la popularidad: '))
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
        precio1 = int(input('Ingrese la cantidad minima de dinero: '))
        precio2 = int(input('Ingrese la cantidad maxima de dinero que le interesa: '))
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
        banda = input('Ingrese el nombre de la banda o artista: ').lower()
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
    #Cerramos lo que quede abierto y retornamos la lista
    informacionDisco.close()
    return listaFinal

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
#Hacemos una variable que almacenara los datos que retorne la funcion
listaFinalDiscos = filtrarDiscos(listaDeDiscos,respuesta)
#Nos aseguramos de cerrar todo
discos.close()
#Si se encontraron discos que cumplen los requisitos, se lo informamos al usuario
if len(listaFinalDiscos) > 0:
    print('Los discos que le podrian interesar son:')
    for elemento in listaFinalDiscos:
        print('-',elemento)
#Si no hubiera ningun disco con las caracteristicas buscadas se lo informamos
if len(listaFinalDiscos) == 0:
    print('No se ha podido encontrar algun disco con esas caracteristicas.')
    
        
                

            
    
    
    


        
    
    

        



                          


                    
            
                    
                    
                
                
                
            
            
            
            
            
                
            
 
    

    
   
            
            
