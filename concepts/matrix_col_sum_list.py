# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

# Printa a matriz
for i in range(3):
    print(matriz[i])

somaColuna = []

# Percorre as colunas e acumula na variável soma
for coluna in range(3):
    soma = 0
    for lin in range(3):
        soma += matriz[lin][coluna]
    somaColuna.append(soma)

# Output
print(f'\nTotal por Coluna: {somaColuna}')