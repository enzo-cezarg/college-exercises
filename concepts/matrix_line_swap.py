# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

print('Matriz original: ')

# Printa a matriz
for i in range(3):
    print(matriz[i])

print()

# Troca as linhas por meio de variável auxiliar
aux = matriz[0]
matriz[0] = matriz[2]
matriz[2] = aux
print('Matriz após a troca de linhas: ')

for i in range(3):
    print(matriz[i])