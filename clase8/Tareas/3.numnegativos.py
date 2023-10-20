numeros = []
while verdadero:
    numero = int(input("Ingrese un número (ingrese un número negativo para detenerse): "))
    if numero < 0:
        break
    numeros.append(numero)
print("Lista original:")
print(numeros)

numeros_sin_duplicados = list(set(numeros))

print("\nLista sin números duplicados:")
print(numeros_sin_duplicados)