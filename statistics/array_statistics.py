import random

# Inicialização da lista vazia
lista = []

# Adição dos valores aleatórios e print da lista
for i in range(1, 31):
    lista.append(random.randint(1, 500))
print(lista)

# Inicialização da variável contadora de pares
pares = 0

# Verificação de pares
for num in lista:
    if num % 2 == 0:
        pares += 1

# Output do programa
print(f'Maior número: {max(lista)}')
print(f'Quantidade de pares: {pares}')