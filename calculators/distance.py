import math

def distancia(x1, y1, x2, y2):
    """Calcula a distância entre dois pontos no plano"""
    dX = x1-x2
    dY = y1-y2
    dist = math.sqrt(dX**2 + dY**2)
    return dist

print('> Informe os valores no plano cartesiano: ')
# Primeiro ponto
print('===='*10)
print('Primeiro ponto:')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
# Segundo ponto
print('===='*10)
print('Segundo ponto:')
x2 = float(input('x2: '))
y2 = float(input('y2: '))

# Output do programa
print('===='*10)
print(f'Distância entre os pontos: {distancia(x1, y1, x2, y2):.2f}')