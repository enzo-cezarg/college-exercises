import math, sys

# Entrada de dados
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))

# Cálculo do delta
delta = math.pow(b, 2) - 4*a*c

# Verificação das raízes em função do delta
if delta < 0:
    print('\nA equação não tem raízes reais.')
    sys.exit()

if delta == 0:
    print('\nDelta igual a 0. As duas raízes são iguais.')

# Primeira raíz da equação
x1 = (-(b) + math.sqrt(delta)) / (2*a)

# Segunda raíz da equação
x2 = (-(b) - math.sqrt(delta)) / (2*a)

# Saída de dados
print('\nPrimeira raíz:', x1, '\nSegunda raíz:', x2)