def pascal(linhas):
    for linha in range(linhas):
        for coluna in range(linha+1):
            valor = binomial(linha, coluna)
            print(f'{valor} ', end="")
        print('\n')

def binomial(n, k):
    """Retorna o resultado do coeficiente binomial mais eficientemente"""
    # Tempo de execução pode ser verificado com a diretiva %timeit do Google Colab
    prod = 1
    total = k
    if n - k < k:
        total = n - k
    for i in range(1, total+1):
        prod = prod * ((n + 1 - i)/i)
    return int(prod)

# Entrada de dados
l = int(input('Quantas linhas devem ser construídas? '))

# Output da função
pascal(l)