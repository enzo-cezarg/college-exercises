soma = 0

while(soma == 0):
    num = int(input('Digite um número inteiro de 1 a 9: '))
    if not(num > 0 and num < 10):
        print('Número fora do intervalo! Tente novamente.')
        print('===='*10)
        continue
    else:
        print('===='*10)
        print(f'Somando: {num} + {num + num * 10} + {num + num * 10 + num * 100}')
        soma = num + num + num * 10 + num + num * 10 + num * 100

        print(f'Resultado: {soma}')