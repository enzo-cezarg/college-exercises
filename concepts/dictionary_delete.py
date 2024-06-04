dic = {}
dic['Fulano'] = '99684-3782'
dic['Beltrano'] = '98907-6534'
dic['Ciclano'] = '99078-2342'

nome = ''
while nome != 'q!':
    print(f'Tamanho do dicionário: {len(dic)}')
    print(dic)
    nome = input('Nome a remover (q! para sair): ')
    if nome != 'q!':
        if nome in dic:
            del dic[nome]
            print('Nome removido!')
        else:
            print('Nome não encontrado')