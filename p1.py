lista =['000','00','0101']
contador = 0
verificador = 0

for elemento in lista:
    for caracter in elemento:
        if(caracter == '0'):
            contador += 1
            verificador +=1
    if(verificador%2 == 0):
        print('si sirven')
    verificador = 0
    
