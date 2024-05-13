import random

# Sorteio de um número aleatório
numSort = random.randint(0, 100)

# Inicialização da variável
acertou = False

# Tentativas do usuário de acertar o número sorteado
for i in range(0, 10):
    chute = int(input('Qual o seu chute? (0 a 100) '))
    
    # Verificação do número digitado
    if not(chute >= 0 and chute <= 100):
        print('Chute inválido! Valores devem estar entre 0 e 100!')
    else:
        if chute == numSort:
            acertou = True
            break
        elif chute > numSort:
            print('Errou! DICA: seu chute é MAIOR do que o número sorteado')
        else:
            print('Errou! DICA: seu chute é MENOR do que o número sorteado')

    print('===='*15)

if acertou == True:
    print(f'\nParabéns! Você digitou o número correto em {i} tentativas!')
else:
    print(f'\nQue pena... Você perdeu! O número sorteado era {numSort}')