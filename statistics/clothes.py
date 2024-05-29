import random

# Inicialização das listas
tamanhos = ['P', 'M', 'G']
cores = ['Branco', 'Preto', 'Azul']
roupas = []

# Geração aleatória de tamanhos e cores das roupas
for i in range(50):
    tamanho = random.randint(0, 2)
    cor = random.randint(0, 2)
    # Inserção da tupla ao final da lista
    roupas.append((tamanhos[tamanho], cores[cor]))

# Inicialização de listas contadoras
maisV = [0, 0, 0]
corP = [0, 0, 0]

# Para cada tupla, acrescenta o tamanho e a cor na lista contadora correspondente
for t in roupas:
    if t[0] == 'P':
        maisV[0] += 1
    elif t[0] == 'M':
        maisV[1] += 1
    elif t[0] == 'G':
        maisV[2] += 1

    if t[1] == 'Branco':
        corP[0] += 1
    if t[1] == 'Preto':
        corP[1] += 1
    if t[1] == 'Azul':
        corP[2] += 1

# Printa as roupas vendidas
for i in range(50):
    print(roupas[i])

print('===='*10)
# Verifica qual o tamanho mais vendido
if maisV[0] > maisV[1] and maisV[0] > maisV[2]:
    print('O tamanho mais vendido foi P')
elif maisV[1] > maisV[0] and maisV[1] > maisV[2]:
    print('O tamanho mais vendido foi M')
elif maisV[2] > maisV[0] and maisV[2] > maisV[1]:
    print('O tamanho mais vendido foi G')
else:
    print('Empate entre dois tamanhos!')

# Output do número de peças de tamanho M vendidas
print(f'Foram vendidos um total de {maisV[1]} peças de tamanho M')

# Verifica qual a cor mais vendida
if corP[0] > corP[1] and corP[0] > corP[2]:
    print(f'A cor preferida foi Branco')
elif corP[1] > corP[0] and corP[1] > corP[2]:
    print(f'A cor preferida foi Preto')
elif corP[2] > corP[0] and corP[2] > corP[1]:
    print(f'A cor preferida foi Azul')
else:
    print('Empate entre duas cores!')