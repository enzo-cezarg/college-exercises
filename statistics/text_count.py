import string

# Entrada de dados do usuário
frase = input('Digite uma frase para contar os caracteres: ')

# Inicialização de uma lista vazia
letras = []

# Verificação de cada letra da frase
for letra in frase.lower():
    if not(letra == " "):
        if letra in letras:
            continue
        else:
            letras.append(letra)

# Ordena as letras e printa cada uma com a quantidade de vezes que apareceu
for letra in sorted(letras):
    print(f'{letra}: {frase.lower().count(letra)} || ', end="")

# Inicialização de dois conjuntos: alfabeto e letras usadas
print()
alfabeto = set()
usadas = set(letras)

# Passa por todas as letras e adiciona cada uma separadamente ao conjunto alfabeto
i = 0
for letra in string.ascii_lowercase:
    alfabeto.add(string.ascii_lowercase[i])
    i += 1

# Faz o cálculo da diferença dos conjuntos, ordena e printa as letras não usadas
print(f'Letras não usadas: {sorted(alfabeto.difference(usadas))}')