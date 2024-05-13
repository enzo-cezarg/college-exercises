# Entrada de dados
saldoM = float(input('Digite o saldo médio da sua conta corrente: R$ '))

# Cálculo do limite e saída de dados
if saldoM < 500.0:
    print('Não há limite.')

if saldoM >= 500.0 and saldoM < 1000.0:
    print('Limite: R$', round(saldoM * 0.08, 2))

if saldoM >= 1000.0:
    print('Limite: R$', round(saldoM * 0.15, 2))