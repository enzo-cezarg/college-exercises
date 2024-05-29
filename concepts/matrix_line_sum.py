# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

# Inicialização da variável soma
soma = 0

# Printa a matriz
for i in range(3):
    print(matriz[i])

# Usuário informa a linha desejada
linha = int(input('Qual linha você deseja somar (1 a 3)? '))

# Percorre a linha e acumula na variável soma
for elemento in range(3):
    soma += matriz[linha-1][elemento]

# Output
print(f'Soma dos elementos da linha: {soma}')