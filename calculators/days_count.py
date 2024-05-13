import sys

# Entrada de dados
mes = int(input('Digite um mês ("1" para janeiro, "2" para fevereiro...): '))
if not(mes >= 1 and mes <= 12):
    print('Número inválido! Tente novamente.')
    sys.exit()

ano = int(input('De qual ano? '))

# Verificação de ano bissexto
if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('Ano bissexto! 29 dias em fevereiro!')
    else:
        print('28 dias no mês.')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('30 dias no mês.')
else:
    print('31 dias no mês.')