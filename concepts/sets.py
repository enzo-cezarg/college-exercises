# Inicialização do conjunto e da variável op
a = set()
op = ""

# Loop que insere ou remove elementos no conjunto
while op != 'q!':
    print(f'Conjunto {a}: ')
    print('Digite um valor a inserir no conjunto')
    op = input('pop para remover um elemento, q! para encerrar: ')
    if op == "pop":
        if len(a) <= 0:
            print('Conjunto está vazio!')
            print('===='*15)
        else:
            v = a.pop()
            print(f'Valor removido: {v}')
            print('===='*15)
    else:
        a.add(op)
        print('===='*15)
print('Programa encerrado!')