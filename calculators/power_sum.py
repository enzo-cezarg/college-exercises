def potencia(a):
    """Retorna a potência do número"""
    return a**2

def somaPotencias(a, b, c):
    """Soma as potências de 3 números especificados"""
    return potencia(a) + potencia(b) + potencia(c)

# Entrada de dados
v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
v3 = int(input('Digite o valor 3: '))

# Utilização da função para somar as potências
result = somaPotencias(v1, v2, v3)

# Output do programa
print('===='*7)
print(f'Soma das potências: {result}')