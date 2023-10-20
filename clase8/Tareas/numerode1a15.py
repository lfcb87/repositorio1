import random

numeros = [random.randint(1, 100) for _ in range(15)]

numeros.sort()
print("\nLista ordenada de menor a mayor:")
print(numeros)