import math

def menorDistancia(x1, y1, x2, y2, x3, y3):
    """Calcula a menor distância entre três pontos no plano"""
    d12 = distancia(x1, y1, x2, y2)
    d13 = distancia(x1, y1, x3, y3)
    d23 = distancia(x2, y2, x3, y3)
    return min(d12, d13, d23)

def distancia(x1, y1, x2, y2):
    """Calcula a distância entre dois pontos no plano"""
    dX = x1-x2
    dY = y1-y2
    dist = math.sqrt(dX**2 + dY**2)
    return dist

print('> Informe os valores no plano cartesiano:')
# Coordenadas do ponto 1
x1 = float(input('Ponto 1 | X: '))
y1 = float(input('Ponto 1 | Y: '))
print('===='*12)
# Coordenadas do ponto 2
x2 = float(input('Ponto 2 | X: '))
y2 = float(input('Ponto 2 | Y: '))
print('===='*12)
# Coordenadas do ponto 3
x3 = float(input('Ponto 3 | X: '))
y3 = float(input('Ponto 3 | Y: '))
print('===='*12)

# Output do programa
print(f'Menor distância entre os pontos: {menorDistancia(x1, y1, x2, y2, x3, y3):.2f}')