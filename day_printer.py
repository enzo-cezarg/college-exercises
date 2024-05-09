# Entrada de dados
dia = int(input('Informe o dia da semana como um valor inteiro (1 a 7): '))

# Verificação do número digitado e saída de dados
if not(dia >=1 and dia <= 7):
    print('Valor Inválido! Fora do intervalo de 1 a 7')
elif dia == 1:
    print('Dia da semana: Domingo')
elif dia == 2:
    print('Dia da semana: Segunda-feira')
elif dia == 3:
    print('Dia da semana: Terça-feira')
elif dia == 4:
    print('Dia da semana: Quarta-feira')
elif dia == 5:
    print('Dia da semana: Quinta-feira')
elif dia == 6:
    print('Dia da semana: Sexta-feira')
else:
    print('Dia da semana: Sábado')