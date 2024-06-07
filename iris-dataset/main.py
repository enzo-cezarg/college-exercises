import matplotlib.pyplot as plt
import random

def carregarDados(arq):
  with open(arq, 'r') as arquivo:
    arquivo.readline()
    dados = [linha[:-1].split(',') for linha in arquivo]
    valores = []
    for linha in range(len(dados)):
      valores.append((float(dados[linha][0]), float(dados[linha][1]), float(dados[linha][2]), float(dados[linha][3]), dados[linha][4]))
    arquivo.close()
  return valores

def misturarValores(lista, quantidade):
  cont = 0
  while cont <= quantidade:
    i = random.randint(0, len(lista)-1)
    j = random.randint(0, len(lista)-1)
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    cont += 1
  return lista

def definirAmostra(lista, indice):
  lista = misturarValores(dados, random.randint(80, 100))
  quant = len(lista) * indice
  amostra = []
  cont = 0
  while cont < quant:
    amostra.append(lista[cont])
    cont += 1
  return amostra

def gravarAmostra(amostra, arq):
  with open(arq, 'w+') as arquivo:
    arquivo.truncate()
    for linha in amostra:
      arquivo.write(f'{linha}\n')
    print('Gravado com sucesso!\n')
    
def contarAmostras(amostra, tiposPlantas):
  cont = [0, 0, 0]
  for linha in amostra:
    if tiposPlantas[0] in linha:
      cont[0] += 1
    elif tiposPlantas[1] in linha:
      cont[1] += 1
    else:
      cont[2] += 1
  return cont

def gerarGrafico(tp, quants):
  plt.bar(tp,quants,color='blue')
  plt.title('Distribuição de amostras por tipo de planta:',color='blue')
  plt.xlabel('Tipos de plantas',color='blue')
  plt.ylabel('Quantidade de amostras',color='blue')
  plt.show()

def analisarAtributos(amostra):
  lista = [[],[],[],[]]
  for item in range(len(amostra)):
    lista[0].append(float(amostra[item][0]))
    lista[1].append(float(amostra[item][1]))
    lista[2].append(float(amostra[item][2]))
    lista[3].append(float(amostra[item][3]))

  print(f'Comprimento da sépala:  Min.: {min(lista[0])} | Máx.: {max(lista[0])} | Média: {sum(lista[0])/len(lista[0]):.2f}')
  print(f'Largura da sépala:      Min.: {min(lista[1])} | Máx.: {max(lista[1])} | Média: {sum(lista[1])/len(lista[1]):.2f}')
  print(f'Comprimento da pétala:  Min.: {min(lista[2])} | Máx.: {max(lista[2])} | Média: {sum(lista[2])/len(lista[2]):.2f}')
  print(f'Largura da pétala:      Min.: {min(lista[3])} | Máx.: {max(lista[3])} | Média: {sum(lista[3])/len(lista[3]):.2f}')

# ====================== Programa principal ====================== #

dados = carregarDados(r'iris-dataset\iris-data.csv')
amostra = definirAmostra(dados, 0.3)
gravarAmostra(amostra, r'iris-dataset\amostra.csv')

tipos = ['Iris-setosa','Iris-versicolor','Iris-virginica']
quant = contarAmostras(amostra,tipos)

i = 0
classe = tipos[0]
maior = quant[0]

print('Resultados:\n')
while i < len(tipos):
  print(f'{tipos[i]} - Amostras: {quant[i]} ({quant[i]*100/len(amostra):.2f}%)')
  if quant[i] > maior:
    maior = quant[i]
    classe = tipos[i]
  i += 1

analisarAtributos(amostra)

print(f'\nTotal de amostras: {len(amostra)}')
print(f'Tipo com mais amostras: {classe}\n')
gerarGrafico(tipos,quant)