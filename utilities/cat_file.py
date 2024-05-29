arq = open('/home/desenvolvimento/Área de Trabalho/python-dev/college-exercises/csv/teste.csv', 'r')

valores = []
for linha in arq:
    valores.append(linha.split(','))
arq.close()

print(valores)