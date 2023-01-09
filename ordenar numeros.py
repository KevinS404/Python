lista = [46.2,42.9,40.4,45.4,46.7,43.6,39.9,46.0,40.2,44.3,46.5,49.3,53.3,44.5,42.5,45.5,47.3,43.9,45.7,47.9,50.2,45.5,52.7,48.4,50.4,45.9,40.1,41.8,44.0,53.4]
lista2 = [35.6,35.7,36.1,37.1,37.2,37.3,37.4,38.3,38.3,39.1,39.1,39.5,39.6,39.9,40.0,40.4,40.7,40.7,40.8,41.1,41.4,41.8,42.0,42.2,44.1,44.2,45.9,46.2,47.9,50.1]
promedio = sum(lista)/len(lista)
promedio2 = sum(lista2)/len(lista2)
varianzaP1 = []
for numero in lista:
    numero = (numero - promedio)**2
    varianzaP1.append(numero)
varianzaP2 = []
for numero in lista2:
    numero = (numero - promedio2)**2
    varianzaP2.append(numero)
    
resultadoVP1 = (sum(varianzaP1)/len(lista))**0.5
resultadoVP2 = (sum(varianzaP2)/len(lista2))**0.5
varianzaMF1 = (sum(varianzaP1)/len(lista)-1)**0.5
varianzaMF2 = (sum(varianzaP2)/len(lista2)-1)**0.5
print('promedio F1:', promedio)
print('promedio F2:', promedio2)
print('varianza poblacional F1:' , resultadoVP1)
print('varianza poblacional F2:' , resultadoVP2)
print('desviacion estandar F1:', varianzaMF1)
print('desviacion estandar F2:', varianzaMF2)

                   
