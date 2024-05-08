# Entrada de dados
dia = int(input('Informe o dia da semana como um valor inteiro (1 a 7): '))

# Verificação do número digitado e atribuição do dia correspondente
if not(dia >=1 and dia <= 7):
    print('Valor Inválido! Fora do intervalo de 1 a 7')
else:
    if dia == 1:
        diaSemana = 'Domingo'
    if dia == 2:
        diaSemana = 'Segunda-feira'
    if dia == 3:
        diaSemana = 'Terça-feira'
    if dia == 4:
        diaSemana = 'Quarta-feira'
    if dia == 5:
        diaSemana = 'Quinta-feira'
    if dia == 6:
        diaSemana = 'Sexta-feira'
    if dia == 7:
        diaSemana = 'Sábado'

# Saída de dados
    print('Dia da semana:', diaSemana)