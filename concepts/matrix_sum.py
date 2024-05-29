# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

# Inicialização da variável soma
soma = 0

# Printa a matriz
for i in range(3):
    print(matriz[i])

# Percorre a matriz e acumula na variável soma
for linha in matriz:
    for elem in linha:
        soma += elem

# Output
print(f'Soma dos elementos da matriz: {soma}')