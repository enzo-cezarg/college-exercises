import sys, math

# Entrada de dados
hInicio = int(input('Qual o horário de início do jogo? (apenas hora)'))
if hInicio > 24 or hInicio < 0:
    print('Valor INVÁLIDO!')
    sys.exit()

mInicio = int(input('Qual o horário de início do jogo? (apenas minuto)'))
if mInicio > 60 or mInicio < 0:
    print('Valor INVÁLIDO!')
    sys.exit()

hFim = int(input('Qual o horário de término do jogo? (apenas hora)'))
if hFim > 24 or hFim < 0:
    print('Valor INVÁLIDO!')
    sys.exit()

mFim = int(input('Qual o horário de término do jogo? (apenas minuto)'))
if mFim > 60 or mFim < 0:
    print('Valor INVÁLIDO!')
    sys.exit()

# Conversão dos valores para minutos
horarioI = (hInicio * 60) + mInicio
horarioF = (hFim * 60) + mFim

# Verificação que identifica se o jogo terminou no mesmo dia
if horarioI < horarioF:
    duracao = horarioF - horarioI
else:
    duracao = 24*60 - horarioI + horarioF

# Saída de dados
print('Horas: ', duracao // 60)
print('Minutos: ', duracao % 60)