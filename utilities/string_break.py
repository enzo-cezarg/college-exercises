# Inicializa a lista
frases = []

# Entrada de dados
for i in range(5):
    frase = input('Digite uma frase: ')
    frases.append(frase.split(' '))

# Printa a lista com as frases separadas
print()
print(frases)

# Printa cada lista interna e depois seus elementos
for frase in frases:
    print(f'Palavras da frase: {frase}')
    for palavra in frase:
        print(palavra, end=" ")
    print('\n')
    print('===='*15)