# Declaração de função que calcula o IMC
def imc(peso, altura):
  return peso / altura ** 2

# Entrada de dados
p = float(input('Digite o seu peso (kg):'))
a = float(input('Digite a sua altura (m): '))

# Output do programa
print(f'IMC: {imc(p, a):.2f}')