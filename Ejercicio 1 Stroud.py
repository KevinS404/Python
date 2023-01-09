"""
ESTE SCRIPT PERMITE SABER SI ROBERT STROUD PUEDE
SALIR DE LA PRISIÓN EJECUTANDO SU PLAN.
AUTORES: Víctor Colombo (20.408.994-9),Kevin Silva (20.495.193-4)
"""

### BLOQUE PRINCIPAL ###
#ENTRADA
 #Se entrega un mensaje al usuario de como utilizar el programa.
print("Al momento de ingresar el mapa, debe ser con letras MAYÚSCULAS y")
print("separando cada letra por espacios.")
print('Cada letra representa lo siguiente:')
print('S = Stroud (solo existe un Robert Stroud)')
print('C = Camino libre')
print('G = Camino con guardia')
print('L = Llave (solo existe una Llave)')
print('S = Salida (solo existe una Salida)')
 #Se solicitan al usuario el mapa y el tiempo disponible.
mapa = input("Ingrese el mapa: ").split()
print("El tiempo de escape debe ser entregado en horas.")
tiempoDisponible = float(input("Ingrese el tiempo de escape: "))

#PROCEDIMIENTO
 #Se definen las siguientes variables, para luego ocuparlas en el código.
tiempoDemora = 0.0
llave = ""
condicionStroud = ""
tiempoDevuelta = 0.0
tiempoNuevoDisp = 0.0
i = 1

 #Se ejecuta la iteración para evaluar cada letra del mapa.
while tiempoDisponible >= 0 and i < len(mapa):
     #Las siguientes sentencias asignan los tiempos respectivos
     #por cada letra del mapa. 
    if tiempoDisponible < 0:            #Se aplica esta condición si en algun momento
        condicionStroud = "arrestado"   #Stroud queda sin tiempo para escapar.
    elif mapa[i] == "C":
        tiempoDisponible = tiempoDisponible-1
        tiempoDemora = tiempoDemora+1
    elif mapa[i] == "G":
        tiempoDisponible = tiempoDisponible-2
        tiempoDemora = tiempoDemora+2
    elif mapa[i] == "L":
        tiempoDisponible = tiempoDisponible-1
        tiempoDemora = tiempoDemora+1
        llave = "encontrada" #Cuando se llegue a la letra "L" del mapa, la llave será encontrada.
     #Esta condición contempla la "Salida", es aquí donde pueden ocurrir 3 casos.
    elif mapa[i] == "S":
        tiempoDisponible = tiempoDisponible-1
        tiempoDemora = tiempoDemora+1
         #Caso1: cuando la llave ha sido encontrada y aún queda tiempo diponible.
        if (llave == "encontrada") and (tiempoDisponible >= 0):
            condicionStroud = "libre"
         #Caso2: cuando la llave ha sido encontrada y el tiempo es insuficiente.
        elif (llave == "encontrada") and (tiempoDisponible < 0):
            condicionStroud = "arrestado"
         #Caso3: cuando la llave no ha sido encontrada.
        else:
            j = i+1
             #Se ejecuta la iteración para evaluar cada letra del mapa
             #despúes de haber encontrado la "Salida".
            while j < len(mapa):
                if mapa[j] == "C":
                    tiempoDevuelta = tiempoDevuelta+1
                elif mapa[j] == "G":  
                    tiempoDevuelta = tiempoDevuelta+2
                elif mapa[j] == "L":                  #En este momento Stroud se devulve a la "Salida",
                    tiempoDevuelta = tiempoDevuelta+1 #por lo tanto el tiempo de regreso seria la mitad
                    tiempoDevuelta = tiempoDevuelta+(tiempoDevuelta/2) #del recorrido anteriormente.
                    tiempoDemora = tiempoDemora+tiempoDevuelta
                    tiempoNuevoDisp = tiempoDisponible-tiempoDevuelta
                    tiempoDisponible = 0.0
                     #Puede que ha Stroud no le alcance el tiempo. Se deberán evaluar dos situaciones.
                    if tiempoNuevoDisp < 0:
                        condicionStroud = "arrestado"
                    elif tiempoNuevoDisp >= 0:
                        condicionStroud = "libre"
                j = j+1
                i = j
            
            
    i = i+1
 #Sentencia que condiciona el tiempo si se ingresa uno negativo por parte del usuario.
if tiempoDisponible <0:
    condicionStroud = "arrestado"

#SALIDA
 #Se lee la condición de Stroud para luego imprimir los tiempos en horas y minutos si
 #Stroud logra escapar de la prisión.
if condicionStroud == "libre":
    if (tiempoDisponible == 0)and(tiempoNuevoDisp >= 0):
        minutosDemora = int((tiempoDemora%1)*60)
        tiempoDemora = int(tiempoDemora)
        minutosNuevoDisp = int((tiempoNuevoDisp%1)*60)
        tiempoNuevoDisp = int(tiempoNuevoDisp)
        print("Stroud a logrado escapar.")
        print("Demoró", tiempoDemora, "hora(s) con", minutosDemora, "minutos y le quedaron")
        print(tiempoNuevoDisp, "hora(s) con", minutosNuevoDisp, "minutos disponibles.")
    elif (tiempoDisponible >= 0)and(tiempoNuevoDisp == 0):
        minutosDemora = int((tiempoDemora%1)*60)
        tiempoDemora = int(tiempoDemora)
        minutosDisponible = int((tiempoDisponible%1)*60)
        tiempoDisponible = int(tiempoDisponible)
        print("Stroud a logrado escapar.")
        print("Demoró", tiempoDemora, "hora(s) con", minutosDemora, "minutos y le quedaron")
        print(tiempoDisponible, "hora(s) con", minutosDisponible, "minutos disponibles.")
elif condicionStroud == "arrestado":
    print("Stroud no logra escapar.")


        
