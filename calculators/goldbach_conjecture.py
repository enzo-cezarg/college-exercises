# Leitura do número de pares
quant = int(input('Informe a quantidade de números pares: '))
while quant <= 0:
    print('O valor deve ser positivo.')
    quant = int(input('Informe a quantidade de números pares: '))
print('===='*15)

num = 4
pares = 1

# Loop de verificação e output do programa
while pares <= quant:
    parte1 = num // 2
    parte2 = parte1

    while(parte2 <= parte1):
        contParte1 = 0
        i = 1

        while i <= parte1:
            if parte1 % i == 0:
                contParte1 += 1
            i += 1

        if contParte1 == 2:
            i = 1
            contParte2 = 0
            while i <= parte2:
                if parte2 % i == 0:
                    contParte2 += 1
                i += 1
            if contParte2 == 2:
                print(f'Número: {num:3} | Primo 1: {parte1:3} | Primo 2: {parte2:3}')
                pares += 1
                break

        parte1 += 1
        parte2 -= 1
    num += 2