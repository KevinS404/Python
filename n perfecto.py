def esPerfecto(n):
    suma = 0
    for numero in range(1,n):
        if n % numero == 0:
            suma = suma + numero
    return suma == n

m = int(input("Ingrese la cantidad de numeros perfectos que desea saber: "))

listaNumeroPerfectos = []
anterior = 1
aux = anterior
siguiente = (anterior *2)**2
largo = range(aux,siguiente)
largoLista = len(listaNumeroPerfectos)
while largoLista < m:
    for numero in largo:
        if esPerfecto(numero):
            listaNumeroPerfectos.append(numero)
        largoLista = len(listaNumeroPerfectos)
        if largoLista == m:
            break

    anterior = siguiente
    aux = anterior
    siguiente = (anterior *2)**2
    largo = range(aux,siguiente)
    largoLista = len(listaNumeroPerfectos)
        
                
    

print(listaNumeroPerfectos)
