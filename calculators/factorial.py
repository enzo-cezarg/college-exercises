# Leitura do valor desejado
num = int(input('Digite um número para calcular o seu fatorial: '))

# Inicialização das variáveis
fat = 1
aux = 2

# Loop de cálculo do fatorial
while aux <= num:
    fat = fat * aux
    aux += 1

# Output do programa
print(f'{num}! = {fat}')