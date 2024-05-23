# Entrada de dados
num = int(input('Digite um número para descobrir seus divisores: '))

# Inicialização da variável auxiliar
aux = num

# Loop para fazer o cálculo de divisores e output do programa
print('\nDivisores:', end=" ")
while aux >= 1:
    if num % aux == 0:
        print(f'| {aux} ', end="")
    aux -= 1
print('|')