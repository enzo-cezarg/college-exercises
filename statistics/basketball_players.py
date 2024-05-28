jogadores = []
cont = 1

while cont <= 3:
    print(f'Jogador {cont}: ')
    nome = input('Nome: ')
    pontos = int(input('Pontos: '))
    assist = int(input('Assistências: '))
    rebotes = int(input('Rebotes: '))

    jogadores.append((nome, pontos, assist, rebotes))
    cont = cont + 1

print('===='*20)
print(jogadores)
estatisticas = []

for dados in jogadores:
    soma = 0
    for i in range(1, 4):
        soma += dados[i]
    media = soma/3
    estatisticas.append((dados[0], media))

print('===='*20)
print(estatisticas)

melhor = estatisticas[0]
for item in estatisticas:
    if item[1] > melhor[1]:
        melhor = item

print(f'Melhor jogador: {melhor}')