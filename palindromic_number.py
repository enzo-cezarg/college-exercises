import math

# Entrada de dados
num = int(input('Digite um valor de 4 dígitos: '))

# Verificação se o número está no intervalo correto
if num < 1000 or num > 9999:
    print('Número INVÁLIDO')
else:
    mil = math.trunc(num / 1000)
    cen = math.trunc(num % 1000 / 100)
    dez = math.trunc(num % 1000 % 100 / 10)
    uni = math.trunc(num % 1000 % 100 % 10)

# Verificação se o número é um palíndromo e saída de dados
    palind = uni * 1000 + dez * 100 + cen * 10 + mil * 1
    if num == palind:
        print('O número', num, 'é um palíndromo')
    else:
        print('O número', num, 'não é um palíndromo')