import sys

# Entrada de dados
n1 = float(input('Digite a primeira nota do aluno: '))
if not(n1 >= 0.0 and n1 <= 10.0):
    print('Valor Inválido! Fora do intervalo de 0 a 10')
    sys.exit()

n2 = float(input('Digite a segunda nota do aluno: '))
if not(n2 >= 0.0 and n2 <= 10.0):
    print('Valor Inválido! Fora do intervalo de 0 a 10')
    sys.exit()

n3 = float(input('Digite a terceira nota do aluno: '))
if not(n3 >= 0.0 and n3 <= 10.0):
    print('Valor Inválido! Fora do intervalo de 0 a 10')
    sys.exit()

# Procedimentos para deixar a maior nota na variável 'n1'
if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux

if n3 > n1:
    aux = n3
    n3 = n1
    n1 = aux

# Cálculo da média ponderada
mediaP = (n1 * 5.0 + n2 * 2.5 + n3 * 2.5) / 10

# Saída de dados
print('Média ponderada do aluno: ', mediaP)