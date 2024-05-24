# Entrada de dados
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

# Inicialização de variáveis
menor = 0
maior = 0
soma = 0

if a == b:
    print('Números iguais! Intervalo inexistente.')
else:
    # Verificação do maior número
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    
    # Output do programa 1
    print(f'A soma dos ímpares no intervalo de {menor} e {maior} é: ', end="")

    # Loop de cálculo da soma
    while menor <= maior:
        if menor % 2 != 0:
            soma += menor
        menor += 1

    # Output do programa 2
    print(soma)