# Jogo da forca

import random

def sorteio():
    """Sorteia uma palavra aleatória dentro de uma lista predefinida"""
    return random.choice(["abacaxi", "brincar", "cerebro", "devaneio", "estrela", "floresta",
        "golfinho", "harmonia", "ilusao", "jornada", "kiwi", "liberdade", "magia", "natureza",
        "oceano", "passaro", "quimera", "riqueza", "saudade", "tempestade", "universo", "vento",
        "xadrez", "abismo", "brilho", "chuva", "canino", "delfim", "enigma", "fenix", "zumbido"])

def forca(vidas):
    """Desenha a forca e verifica o número de vidas"""
    if vidas == 0:
        print('''
       +---+   
       |   |   
       0   |    
      /|\  |    
      / \  |   
           |    
    ==========
    ''', end="")
    elif vidas == 1:
        print('''
       +---+   
       |   |   
       0   |    
      /|\  |    
      /    |   
           |    
    ==========
    ''')
    elif vidas == 2:
        print('''
       +---+   
       |   |   
       0   |    
      /|\  |    
           |   
           |    
    ==========
    ''')
    elif vidas == 3:
        print('''
       +---+   
       |   |   
       0   |    
      /|   |    
           |   
           |    
    ==========
    ''')
    elif vidas == 4:
        print('''
       +---+   
       |   |   
       0   |    
       |   |    
           |   
           |    
    ==========
    ''')
    elif vidas == 5:
        print('''
       +---+   
       |   |   
       0   |    
           |    
           |   
           |    
    ==========
    ''')
    else:
        print('''
       +---+   
       |   |   
           |    
           |    
           |   
           |    
    ==========
    ''')
            
# 1. Sorteia a palavra
palavra = sorteio()
# 2. Gerar a palavra com _

# Letras já adivinhadas
adivinhada = '_'*len(palavra)
# Número de vidas
vidas = 6
# Letras que já foram escolhidas
letras = ''

jogoAtivo = True
# 3. Enquanto o jogo estiver ativo
while jogoAtivo == True:
    # 4. Exibir o estado do jogo
    print()
    forca(vidas)
    print(f'Palavra: {adivinhada}\n')
    print(f'Letras já escolhidas: {letras}')

    # 5. Aguarda a digitação de uma letra válida (ainda não escolhida)
    valida = False
    while not(valida):
        letra = input('Escolha uma letra: ')
        if letra not in letras:
            valida = True
            letras += letra
        else:
            print('Esta letra já foi escolhida!')
            print('===='*10)

    # 6. Verifica se a letra está na palavra
    if letra in palavra:
    # - Se estiver, troca o _ correspondente
        for pos in range(0, len(palavra)):
            if letra == palavra[pos]:
                adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]
    else:
    # - Se não estiver, perde uma vida e verifica se o jogador perdeu
        print('Esta letra não está na palavra...')
        print('===='*10)
        vidas -= 1
        if vidas == 0:
            print('===='*10)
            # Mostra a forca e encerra o jogo
            forca(vidas)
            jogoAtivo = False
            print('\n> Você perdeu!')

            # Mostra a palavra sorteada
            print(f'A palavra sorteada era: {palavra}')

    # 7. Verifica se o jogador ganhou
    if '_' not in adivinhada:
        forca(vidas)
        print(f'Palavra: {adivinhada}')
        print('Parabéns! Você ganhou!')
        jogoAtivo = False