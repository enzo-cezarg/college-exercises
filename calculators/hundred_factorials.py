# Cálculo do fatorial dos primeiros 100 números naturais
for i in range(1,101):
    fat = 1
    for j in range(1, i+1):
        fat *= j
    print(f'{i:3}! = {fat}')