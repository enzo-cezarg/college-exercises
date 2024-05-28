def fatorial(num):
    """Retorna o fatorial do número inserido"""
    fat = 1
    for cont in range(1, num+1):
        fat = fat * cont
    return fat

def binomial(n, k):
    """Retorna o resultado do coeficiente binomial (número de possibilidades)"""
    return fatorial(n)//(fatorial(k)*fatorial(n-k))

def binomial2(n, k):
    """Retorna o resultado do coeficiente binomial mais eficientemente"""
    # Tempo de execução pode ser verificado com a diretiva %timeit do Google Colab
    prod = 1
    total = k
    if n - k < k:
        total = n - k
    for i in range(1, total+1):
        prod = prod * ((n + 1 - i)/i)
    return int(prod)

# Entrada de dados do usuário
tot = int(input('Digite o total de exemplos (n): ')) 
sel = int(input('Digite o número de selecionados (k): '))
print('===='*10)

# Output do programa
print(f'> Coeficiente binomial:  {binomial(tot, sel)}')
print('===='*10)
print(f'> Coeficiente binomial2: {binomial2(tot, sel)}')