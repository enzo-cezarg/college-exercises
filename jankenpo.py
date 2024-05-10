import random

# Entrada de dados
jogadaInt = int(input('Faça sua jogada!\n1. Pedra\n2. Papel\n3. Tesoura\n'))

if not(jogadaInt >= 1 and jogadaInt <= 3):
    print('Jogada inválida! Tente novamente.')
else:
    # Conversão do número da jogada para string
    if jogadaInt == 1:
        jogada = 'Pedra'
    elif jogadaInt == 2:
        jogada = 'Papel'
    elif jogadaInt == 3:
        jogada = 'Tesoura'

    # Jogada do computador
    comp = random.choice(['Pedra', 'Papel', 'Tesoura'])

    # Jogo
    if jogada == comp:
        print(f'Você jogou {jogada} e o computador jogou {comp}.\nEmpate!')
    elif jogada == 'Pedra':
        if comp == 'Tesoura':
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do jogador!')
        else:
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do computador!')
    elif jogada == 'Papel':
        if comp == 'Pedra':
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do jogador!')
        else:
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do computador!')
    elif jogada == 'Tesoura':
        if comp == 'Papel':
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do jogador!')
        else:
            print(f'Você jogou {jogada} e o computador jogou {comp}.\nVitória do computador!')