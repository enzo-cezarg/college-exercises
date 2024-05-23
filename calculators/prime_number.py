# Inicialização da variável
num = 0

while num <= 0:
    # Leitura do valor desejado
    num = int(input('Informe um valor natural: '))

    # Inicialização de variáveis
    aux = num
    numDivisores = 0

    if num > 0:
        # Loop de verificação de divisores
        while aux >= 1:
            if num % aux == 0:
                numDivisores += 1
            aux -= 1

        # Verificação do número de divisores
        if numDivisores == 2:
            print('O número é primo!')
        else:
            print('O número NÃO É primo!')
    else:
        print('Número inválido! Tente novamente.')
        print('===='*10)