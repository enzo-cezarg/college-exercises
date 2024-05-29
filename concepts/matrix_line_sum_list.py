# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

# Printa a matriz
for i in range(3):
    print(matriz[i])

somaLinha = []

# Percorre as linhas e acumula na variável soma
for linha in matriz:
    soma = 0
    for elem in linha:
        soma += elem
    somaLinha.append(soma)

# Output
print(f'\nTotal por linha: {somaLinha}')