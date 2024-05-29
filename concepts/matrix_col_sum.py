# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

# Inicialização da variável soma
soma = 0

# Printa a matriz
for i in range(3):
    print(matriz[i])

# Usuário informa a coluna desejada
col = int(input('Qual coluna você deseja somar (1 a 3)? '))

# Percorre a coluna e acumula na variável soma
for elemento in range(3):
    soma += matriz[elemento][col-1]

# Output
print(f'Soma dos elementos da coluna: {soma}')