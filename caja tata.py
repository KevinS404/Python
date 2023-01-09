#Programa que se encarga de entregar la secuencia TATA de mayor tamaño

#BLOQUE DE DEFINICIONES
#necesitamos que nos entreguen el texto que contenga la caja
secuencia = 'ATTTGATGATAATTTATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGATAAATA'
#Definiremos la funcion que se encargara de encontrar la caja TATA
def encontrarCajaTata(secuencia):
    cajaTata = 'TATAAA'
    if not (cajaTata in secuencia):
        return ''
    while cajaTata in secuencia:
        cajaTata = cajaTata + 'AAA'
        if not(cajaTata in secuencia):
            cajaTataNueva = cajaTata
        
        

    return cajaTata

print(encontrarCajaTata(secuencia))  
