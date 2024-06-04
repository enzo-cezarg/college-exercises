dic = {}
dic['Fulano'] = '99684-3782'
dic['Beltrano'] = '98907-6534'
dic['Ciclano'] = '99078-2342'

for k in dic.keys():
    print(f'Chave: {k}')

for v in dic.values():
    print(f'Valor: {v}')

print('\nChaves e valores por ordem de inclusão: ')
for k, v in dic.items():
    print(f'{k:8} -> {v}')

print('\nOrdenado pelas chaves: ')
for k, v in sorted(dic.items()):
    print(f'{k:8} -> {v}')

print('\nOrdenado pelos valores: ')
for k, v in sorted(dic.items(),key=lambda x: x[1]):
    print(f'{k:8} -> {v}')