notas = []

for i in range(0, 15):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)

media = sum(notas)/15
av = [0, 0, 0]

for i in range(0, 15):
    if notas[i] > media:
        av[0] += 1
    if notas[i] == media:
        av[1] += 1
    if notas[i] < media:
        av[2] += 1
    
print('===='*10)
print(f'Acima da média: {av[0]}')
print(f'Na média: {av[1]}')
print(f'Abaixo da média: {av[2]}')