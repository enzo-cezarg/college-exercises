dic = {}
dic['Fulano'] = '99684-3782'
dic['Beltrano'] = '98907-6534'
dic['Ciclano'] = '99078-2342'

nome = ''
while nome != 'q!':
    nome = input('Digite o nome para buscar (digite q! para cancelar): ')
    if nome != 'q!':
        if nome in dic:
            print(f'Telefone: {dic[nome]}')
        else:
            print('Nome não encontrado')