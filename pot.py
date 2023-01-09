bas = 2
exp = 2
if(exp==0):
    print(1)
else:      
    respuesta=bas
    potencia=bas
    for i in range(1,exp):
        for j in range (1,bas):
            respuesta+=potencia
        potencia=respuesta
    print(respuesta)
