# Inicialização da matriz
matriz = [[1,2,4], [2,3,5], [3,4,5]]

print('Matriz original: ')

# Printa a matriz
for i in range(3):
    print(matriz[i])

print()

# Troca as colunas por meio de variável auxiliar
for e in range(3):
    aux = matriz[e][0]
    matriz[e][0] = matriz[e][1]
    matriz[e][1] = aux
print('Matriz após a troca de colunas: ')

for i in range(3):
    print(matriz[i])