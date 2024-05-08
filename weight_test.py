import sys

gen = int(input('Qual o seu gênero?\n1. Masculino\n2. Feminino\n: '))

if gen != 1 and gen != 2:
    print('Número inválido!')
    sys.exit()

alt = float(input('Digite a sua altura (m): '))

if gen == 1:
    print('Seu peso ideal: ', (72.7 * alt - 58))
if gen == 2:
    print('Seu peso ideal: ', (62.1 * alt - 44.7))