import sys, os

# Entrada de dados
salarioBruto = float(input('Digite o valor do salário bruto: '))
if salarioBruto < 1212.0:
    print('Salário inválido! Valor está abaixo do salário mínimo.')
    sys.exit()

dependentes = int(input('Insira o número de dependentes: '))
if dependentes < 0:
    print('Número de dependentes inválido! Tente novamente.')
    sys.exit()

# Tabela de descontos do INSS
if salarioBruto == 1212.0:
    aliquotaInss = 0.075
    parcelaInss = 0
    tetoInss = 90.90

elif salarioBruto > 1212.0 and salarioBruto <= 2427.35:
    aliquotaInss = 0.09
    parcelaInss = 18.18
    tetoInss = 200.28

elif salarioBruto > 2427.35 and salarioBruto <= 3641.03:
    aliquotaInss = 0.12
    parcelaInss = 91
    tetoInss = 345.92

elif salarioBruto > 3641.03:
    aliquotaInss = 0.14
    parcelaInss = 163.82
    tetoInss = 828.39

# Cálculo do valor de contribuição ao INSS
inss = (salarioBruto * aliquotaInss) - parcelaInss
if inss > tetoInss:
    inss = tetoInss

# Tabela de descontos do IRRF
baseCalculo = salarioBruto - inss - (189.59 * dependentes)

if baseCalculo <= 1903.98:
    aliquotaIrrf = 0
    parcelaIrrf = 0

elif baseCalculo > 1903.98 and baseCalculo <= 2826.65:
    aliquotaIrrf = 0.075
    parcelaIrrf = 142.80

elif baseCalculo > 2826.65 and baseCalculo <= 3751.05:
    aliquotaIrrf = 0.15
    parcelaIrrf = 354.80

elif baseCalculo > 3751.05 and baseCalculo <= 4664.68:
    aliquotaIrrf = 0.225
    parcelaIrrf = 636.16

elif baseCalculo > 4664.68:
    aliquotaIrrf = 0.275
    parcelaIrrf = 869.36

# Cálculo do valor de IRRF
irrf = (baseCalculo * aliquotaIrrf) - parcelaIrrf

# Cálculo do salário líquido
salarioLiq = salarioBruto - inss - irrf

# Verifica o sistema operacional e limpa a tela
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

# Saída de dados
print('-------------------------------------------')
print(f'Valor de contribuição ao INSS:  R$ {round(inss, 2)}')
print(f'Valor de descontos do IRRF:     R$ {round(irrf, 2)}')
print('-------------------------------------------')
print(f'  Total do salário líquido:     R$ {round(salarioLiq,2 )}\n')