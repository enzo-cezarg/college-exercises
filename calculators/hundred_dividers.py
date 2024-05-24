# Loop de cálculo dos divisores e output do programa
for i in range(1,101):
    j = 1
    print(f'\n> Número: {i}\nDivisores naturais: ')
    for j in range(j, i+2):
        if i % j == 0:
            print(f' {j} |', end="")
    print('\n')