# Inicialização da variável num
num = 0

while num <= 0:
    # Entrada de dados
    num = int(input('Digite um número inteiro e positivo: '))

    if num > 0:
        # Inicialização das variáveis
        aux = num - 1
        soma = 0

        # Loop para fazer o cálculo de divisores
        while aux >= 1:
            if num % aux == 0:
                soma += aux    
            aux -= 1

        # Verificação se o número digitado é perfeito e output do programa
        print('===='*15)
        if soma == num:
            print('O número é perfeito!\n> A soma dos seus divisores* resultam no próprio número\n* Sem contar ele mesmo')
        else:
            print('O número não é perfeito.\n> A soma dos seus divisores* NÃO resultam no próprio número\n* Sem contar ele mesmo')
    else:
        print('Número inválido! Tente novamente.')
        print('===='*15)