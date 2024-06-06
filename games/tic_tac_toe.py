import random, datetime as dt, os

def jogoDaVelha():
    print('========== Jogo da Velha ==========\n')
    tab = geraTabuleiro()
    escreveTabuleiro(tab)
    jogaUsuario(tab)

    cont = 1
    vencedor = 0

    while cont <= 4:
        jogaComputador(tab)
        vencedor = verificaVencedor(tab)
        if vencedor != 0: 
            break
        escreveTabuleiro(tab)
        jogaUsuario(tab)
        vencedor = verificaVencedor(tab)
        if vencedor != 0:
            break
        cont += 1

    escreveTabuleiro(tab)
    if vencedor == 0: print('Deu velha!')
    elif vencedor == 2: print('O computador venceu!')
    else: print('O usuário venceu!')

    return vencedor

def geraTabuleiro():
    tabuleiro = []
    for col in range(0, 3):
        linha = []
        for lin in range(0, 3):
            linha.append('#')
        tabuleiro.append(linha)
    return tabuleiro

def escreveTabuleiro(tab):
    i = 0
    print('\t    0    1    2')
    for linha in tab:
        print(f'\t{i} {linha}')
        i += 1
    return tab

def valida(valor):
    if valor >= 0 and valor <= 2:
        return True
    else:
        return False

def jogaUsuario(tab):
    print()
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))
    while not(valida(linha)) or not(valida(coluna)) or not tab[linha][coluna]=='#':
        print('Índice fora do intervalo ou célula ocupada!\n')
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
    tab[linha][coluna] = 'X'

def jogaComputador(tab):
    linha = random.randint(0, 2)
    coluna = random.randint(0, 2)
    while tab[linha][coluna] != '#':
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
    tab[linha][coluna] = 'O'

def verificaVencedor(tab):

    resultado = verificaVencedorLinha(tab, 'X')
    if resultado == True: return 1
    resultado = verificaVencedorLinha(tab, 'O')
    if resultado == True: return 2
    resultado = verificaVencedorColuna(tab, 'X')
    if resultado == True: return 1
    resultado = verificaVencedorColuna(tab, 'O')
    if resultado == True: return 2
    resultado = verificaVencedorDiagonal(tab, 'X')
    if resultado == True: return 1
    resultado = verificaVencedorDiagonal(tab, 'O')

    if resultado == True: return 2
    return 0

def verificaVencedorLinha(tab, simbolo):
  for linha in tab:
    cont = 0
    for item in linha:
      if item == simbolo:
        cont = cont + 1
      else:
        cont = 0
        break
    if cont == 3:
      return True
  return False

def verificaVencedorColuna(tabuleiro, caracter):
  col = 0
  while col<=2:
    lin = 0
    cont = 0
    while lin <=2:
      if tabuleiro[lin][col]==caracter:
        cont = cont + 1
      else:
        cont = 0
        break
      lin = lin + 1
    if cont==3:
      return True
    col = col + 1
  return False

def verificaVencedorDiagonal(tab, simbolo):
    cont = 0
    for i in range(3):
        if tab[i][i]==simbolo: cont += 1
        else: break
    if cont == 3: return True

    cont = 0
    for i in range(3):
        if tab[i][2-i]==simbolo: cont += 1
        else: break
    if cont == 3: return True
    
    return False

def gravaVencedor(nome, arq):
    with open(arq, 'a+') as arquivo:
        arquivo.write(f'{nome} : {dt.datetime.now()}\n')
    arquivo.close()
    return None

def leVencedores(arq):
    with open(arq, 'r+') as arquivo:
        for linha in arquivo:
            print(linha)
    return None

# Programa principal ==================================================================================
while True:
    print('\n\n======== MENU ========')
    print('1. Jogar\n2. Ver Vencedores\n0. Sair\n')
    op = input('Selecione uma opção: ')

    if op == '0':
        print('=='*11)
        print('Fim do programa')
        break
    else:
        if op == '1':
            
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")

            vencedor = jogoDaVelha()
            if vencedor == 0: # Empatou
                gravaVencedor('empate', r'games\resultados.csv')
            elif vencedor == 1: # Usuário ganhou
                print()
                nome = input('Informe o seu nome: ')
                gravaVencedor(nome, r'games\resultados.csv')
            else: # Computador ganhou
                gravaVencedor('computador', r'games\resultados.csv')
        else:
            if op == '2':
                print('=='*11)
                leVencedores(r'games\resultados.csv')
                print('=='*11)
            else:
                print('Opção Inválida!')