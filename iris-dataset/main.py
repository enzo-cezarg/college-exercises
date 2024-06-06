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
    

dados = carregarDados(r'iris-dataset\iris-data.csv')
amostra = definirAmostra(dados, 0.3)
gravarAmostra(amostra, r'iris-dataset\amostra.csv')