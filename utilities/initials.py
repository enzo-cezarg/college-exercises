nome = input('Digite um nome completo: ')

iniciais = ''
inicio = True
for letra in nome:
    if inicio:
        iniciais = iniciais + f'{letra}. ' # end="" -- Mantém na mesma linha
        inicio = False
    elif letra == ' ':
        inicio = True

print(f'Iniciais do nome: {iniciais}')