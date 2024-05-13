import random

# Inicialização das variáveis
# Gênero
genero = 0
# Média de renda
somaRenda = 0

# Média da idade de homens com mais de três filhos
somaIdadeMTF = 0
numHomensMTF = 1

# Quantidade de homens com menos de 30 anos
hSubTrinta = 0

# Média do número de filhos
somaNumFilhos = 0

# Renda do homem mais velho
rendaHomemMV = 0
idadeHomemMV = 0

# Idade da mulher com maior renda
idadeMulherMR = 0
rendaMulherMR = 0

# Sorteio dos dados

for i in range(2000):
    # Gênero
    genero = random.randint(1, 2)

    # Renda
    renda = random.randint(0, 25000)
    somaRenda += renda

    # Idade
    idade = random.randint(18, 90)

    # Filhos
    numFilhos = random.randint(0, 6)
    somaNumFilhos += numFilhos

    # Verificações
    if genero == 1:
        if idade < 30:
            hSubTrinta += 1

        if idade > idadeHomemMV:
            idadeHomemMV = idade
            rendaHomemMV = renda

        if numFilhos > 3:
            somaIdadeMTF += idade
            numHomensMTF += 1
    else:
        if renda > rendaMulherMR:
            rendaMulherMR = renda
            idadeMulherMR = idade

print(f'Média de renda: {somaRenda/2000:.2f}')
print(f'Média da idade de homens com mais de três filhos: {somaIdadeMTF/numHomensMTF:.2f}')
print(f'Número de homens com menos de 30 anos: {hSubTrinta}')
print(f'Média do número de filhos: {somaNumFilhos/2000:.2f}')
print(f'Renda do homem mais velho: {rendaHomemMV} | Idade: {idadeHomemMV}')
print(f'Idade da mulher com maior renda: {idadeMulherMR} | Renda: {rendaMulherMR}')