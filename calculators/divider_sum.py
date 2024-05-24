# Entrada de dados
num = int(input('Digite o valor de n: '))

# Inicialização de variáveis
soma = 0
aux = 1

# Loop de realização da soma
while aux <= num:
    soma += (1 / aux)
    aux += 1
print('===='*10)
print(f'A soma de 1/1 + ... + 1/n é: {soma:.2f}')