# Inicialização de variáveis
num = 0
int1 = 0
int2 = 0
int3 = 0
int4 = 0

while num >= 0:
    # Entrada de dados
    num = int(input('Digite um número positivo: '))
    # Verificação do primeiro intervalo
    if (num >= 0) and (num <= 25):
        int1 += 1
        print('Número registrado no intervalo 1!\nCaso deseje sair, digite um número negativo.')
        print('===='*15)
    # Verificação do segundo intervalo
    if num >= 26 and num <= 50:
        int2 += 1
        print('Número registrado no intervalo 2!\nCaso deseje sair, digite um número negativo.')
        print('===='*15)
    # Verificação do terceiro intervalo
    if num >= 51 and num <= 75:
        int3 += 1
        print('Número registrado no intervalo 3!\nCaso deseje sair, digite um número negativo.')
        print('===='*15)
    # Verificação do quarto intervalo
    if num >= 76 and num <= 100:
        int4 += 1
        print('Número registrado no intervalo 4!\nCaso deseje sair, digite um número negativo.')
        print('===='*15)
    # Verificação de intervalo inválido
    if num > 100:
        print('Número fora do intervalo! Não será contabilizado...')
        print('===='*15)
# Output do programa
print('===='*15)
print('Final do programa! A quantidade de números contados foi: ')
print(f'Intervalo 1 (0 a 25): {int1:2}  | Intervalo 3 (51 a 75): {int3:2}\nIntervalo 2 (26 a 50): {int2:2} | Intervalo 4 (76 a 100): {int4:2}')