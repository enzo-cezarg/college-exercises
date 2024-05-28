# Declaração da função que calcula os juros com parâmetros padrão
def calculaJuros(base, taxa=0.1, tempo=12):
    """Retorna o valor dos juros baseado na base de cálculo, taxa e tempo"""
    return base * taxa * tempo

# Output dos valores padrão da função
print('> Valores padrão: Juros = 10% | Meses = 12')
print('===='*12)
# Entrada de dados do usuário
b = input('Digite a renda base: ')
tax = input('Digite a taxa de juros (%): ')
t = input('Quantos meses? ')

# Verificação de valores vazios
if tax.strip() == "":
    if t.strip() == "":
        # Caso de omissão de taxa e tempo
        res = calculaJuros(int(b))
    else:
        # Caso de omissão de taxa
        res = calculaJuros(int(b), tempo=int(t))
else:
    if t.strip() == "":
        # Caso de omissão de tempo
        res = calculaJuros(int(b), float(tax)/100)
    else:
        # Caso sem omissão de valor
        res = calculaJuros(int(b), float(tax)/100, int(t))

# Output do programa e formatação
print('===='*12)
print(f'> Valor total de juros: R${res:.2f}')
print(f'> Montante da aplicação: R${res + int(b):.2f}')