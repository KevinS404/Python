n = int(input('ingrese un numero entero positivo: '))
lista = []
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    print(factorial)
    lista.append(factorial)
    i = i + 1

print(lista)
