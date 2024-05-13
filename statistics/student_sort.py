import random

# Introdução feita ao usuário
print('Pesquisa: idade, semestre e curso.\nObjeto de pesquisa: 50 alunos de Engenharia')
print('=============================================\n')

# Inicialização das variáveis
somaIdade = 0
maiorIdade = 0
alunosQui = 0
cursoMV = ''

for i in range(1, 51):
    # Sorteio de valores para as variáveis
    if i % 2 == 0:
        idade = random.randint(18, 50)
    else:
        idade = random.randint(18, 25)
    curso = random.choice(['Engenharia de Software',  'Engenharia de Pesca', 'Engenharia Mecatrônica', 'Engenharia Civil'])
    semestre = random.randint(1, 8)

    if idade > maiorIdade:
        maiorIdade = idade
        cursoMV = curso

    somaIdade = somaIdade + idade

    if semestre == 5:
        alunosQui = alunosQui + 1

mediaIdade = somaIdade / 50

print(f'A média de idade dos alunos é {mediaIdade}')
print(f'O curso do aluno mais velho é {cursoMV} e ele tem {maiorIdade} anos')
print(f'Quantidade de alunos no quinto semestre é {alunosQui}')