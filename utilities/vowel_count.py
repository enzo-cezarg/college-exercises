palavra = input('Insira uma palavra para contar as vogais: ')

vogais = 'aeiouAEIOU'
totalVogais = 0

for letra in palavra:
    if letra in vogais:
        totalVogais += 1

print(f'Total de vogais: {totalVogais}')