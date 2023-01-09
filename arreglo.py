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


        

