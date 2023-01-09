#Este programa se encarga de entregar las temperaturas mas altas del año
#Esta lista almacena las temperaturas del año
TEMPERATURAS_MAXIMAS = [0,3,677,-1,204,0.6] 
#Esta funcion se encargara de ordenar la lista de mayor a menor para poder hacer
#el proceso mas facil
def ordenarLista(TEMPERATURAS_MAXIMAS):
    i = 0
    while i <len(TEMPERATURAS_MAXIMAS):
        j = 0
        while j < len(TEMPERATURAS_MAXIMAS)-1:
            if TEMPERATURAS_MAXIMAS[j]<TEMPERATURAS_MAXIMAS[j+1]:
                maximo = TEMPERATURAS_MAXIMAS[j+1]
                minimo = TEMPERATURAS_MAXIMAS[j]
                TEMPERATURAS_MAXIMAS[j+1] = minimo
                TEMPERATURAS_MAXIMAS[j] = maximo
                j = j + 1

            else:
                j = j + 1

        i = i + 1

    return TEMPERATURAS_MAXIMAS
#Guardamos la lista ordenada en una nueva variable
TemperaturasOrdenadas = ordenarLista(TEMPERATURAS_MAXIMAS)
#Una vez ordenada la lista le pedimos la cantidad de dias que la persona quiere
#ver
n = int(input('ingrese la cantidad de dias que quiere ver:'))
#Con esta variable haremos que el programa imprima n cantidad de dias para que
#el usuario lo lea
k = 0
while k < n :
    print(TemperaturasOrdenadas [k])
    k = k + 1
    
