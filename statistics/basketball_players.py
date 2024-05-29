# Inicialização de uma lista vazia que conterá os jogadores
jogadores = []
cont = 1

# Entrada dos dados dos jogadores
while cont <= 3:
    print(f'Jogador {cont}: ')
    nome = input('Nome: ')
    pontos = int(input('Pontos: '))
    assist = int(input('Assistências: '))
    rebotes = int(input('Rebotes: '))

    # Inserção das tuplas ao final da lista
    jogadores.append((nome, pontos, assist, rebotes))
    cont = cont + 1

print('===='*20)
print(jogadores)
# Inicialização de uma lista vazia que conterá o nome do jogador e a média dele
estatisticas = []

# Para cada tupla será calculada a média de pontos do jogador
for tupla in jogadores:
    soma = 0
    for i in range(1, 4):
        soma += tupla[i]
    media = soma/3
    # Inserção do nome do jogador e sua média ao final da lista
    estatisticas.append((tupla[0], media))

print('===='*20)
print(estatisticas)

# Comparação das médias dos jogadores
melhor = estatisticas[0]
for item in estatisticas:
    if item[1] > melhor[1]:
        melhor = item

# Output do programa
print(f'Melhor jogador: {melhor}')