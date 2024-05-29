# Abre o arquivo para 'append+'
arqAlturas = open(r'C:\Users\enzoo\Desktop\dev\python\college-exercises\csv\alturas.txt', 'a+')
# Deleta todo o conteúdo de dentro do arquivo
arqAlturas.truncate(0)

# Escreve o conteúdo digitado pelo usuário no arquivo
for i in range(1, 6):
    nome = input(f'Digite o nome da {i}a pessoa: ')
    altura = float(input(f'Digite a altura da {i}a pessoa (m): '))

    arqAlturas.write((f'{nome}, {altura}\n'))

# Inicialização da lista
dados = []

# Fecha o arquivo para salvar seu conteúdo e abre novamente no modo de leitura
arqAlturas.close()
arqAlturas = open(r'C:\Users\enzoo\Desktop\dev\python\college-exercises\csv\alturas.txt', 'r')

# Conversão das strings do arquivo para tuplas
for linha in arqAlturas:
    valores = linha.split(',')
    tupla = (valores[0], float(valores[1]))
    dados.append(tupla)

# Inicialização de variáveis
soma = 0
maiorA = 0
maiorN = ''

# Compaaração das alturas
for t in dados:
    soma += t[1]

    if t[1] > maiorA:
        maiorN = t[0]
        maiorA = t[1]

# Verificação se há empate de alturas
contMA = 0
for t in dados:
    if t[1] == maiorA:
        contMA += 1

# Cálculo da média
media = soma/5

# Output do programa e verificação de empate
print(f'A média de altura é {media:.2f}')
if contMA == 1:
    print(f'A pessoa mais alta é {maiorN}')
else:
    print('Houve um empate de alturas!')
    
# Fecha o arquivo
arqAlturas.close()