# Entrada de dados
precoCusto = float(input('Digite o preço de custo: R$'))

if precoCusto <= 0:
    print('Preço Inválido!')
else:
    
# Cálculo da porcentagem do lucro / preço de venda:
    if precoCusto < 10.0:
        precoVenda = precoCusto * 1.7

    if precoCusto >= 10.0 and precoCusto < 30.0:
        precoVenda = precoCusto * 1.5

    if precoCusto >= 30.0 and precoCusto < 50.0:
        precoVenda = precoCusto * 1.4

    if precoCusto >= 50:
        precoVenda = precoCusto * 1.3

# Saída para o usuário
    print('Preço de venda: R$', precoVenda)