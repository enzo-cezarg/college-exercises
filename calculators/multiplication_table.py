# Loop de cálculo de tabuada e output do programa
for num in range(1, 11):
    print(f'> Tabuada do {num}:')
    for valor in range(1, 11):
        print(f'{num} x {valor:2} = {num*valor}')
    print('\n')