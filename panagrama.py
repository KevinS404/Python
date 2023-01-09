#Este programa se encarga de determinar si una oracion es un panagrama o no
#Primero que nada crearemos un string con todas las letras del alfabeto
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#ahora pediremos que ingresen la oracion que desea comprobar si es un panagrama
#Tambien nos aseguraremos de que las mayusculas no sean un problema
oracion = input('ingrese la oracion que desea comprobar: ').lower()
print(oracion)

i = 0
while i < len(oracion):
    j = 0
    while j < len(alfabeto):
        if oracion[i] == alfabeto[j]:
            alfabeto.remove(alfabeto[j])
        j = j + 1
    i = i + 1
if len(alfabeto) == 0:
    print('la oracion que usted introdujo es un panagrama')

if len(alfabeto) != 0:
    print('la oracion no es un panagrama porque le faltan estas letras:')
    print(alfabeto)
    
    
