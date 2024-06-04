dic = {}

dic['Fulano'] = '99684-3782'
dic['Beltrano'] = '98907-6534'
dic['Ciclano'] = '99078-2342'

print(dic.keys())
print(dic.values())
print(dic.items())

print(f'Telefone de Fulano: {dic.get('Fulano')}')
print(f'Telefone de Veltrano: {dic.get('Veltrano')}')