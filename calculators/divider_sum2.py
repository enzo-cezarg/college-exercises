# Entrada de dados
num = int(input('Quantos termos você gostaria de somar? '))

# Inicialização de variáveis
soma = 0
auxN = 2
auxD = 1
contTermos = 1

# Loop de realização da soma
while contTermos <= num:
    soma += (auxN / auxD)
    auxD += 2
    auxN += 2
    contTermos += 1

# Output do programa
print('===='*10)
print(f'A soma de 2/1 + 2+2/1+2 ... + n+2/n+1 é: {soma:.2f}')