import math

numero = int(input('Digite um valor de 4 dígitos: '))
mil = math.trunc(numero/1000)
cen = math.trunc(numero%1000/100)
dez = math.trunc(numero%1000%100/10)
un = math.trunc(numero%1000%100%10)

print(un, dez, cen, mil)