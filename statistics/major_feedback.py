import random

lista = []
for i in range(0, 25):
    lista.append(random.randint(1, 5))
print(f'Notas: {lista}')
print('===='*20)

quantidade = [0, 0, 0, 0, 0]
conceito = ['Péssimo', 'Ruim', 'Regular', 'Bom', 'Excelente']

for i in range(0, 5):
    quantidade[i] = lista.count(i+1)
    print(f'{conceito[i]}: {quantidade[i]}')