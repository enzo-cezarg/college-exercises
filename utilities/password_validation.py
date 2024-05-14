import string

senha = input('Senha: ')

maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8:
    print('Erro: senha muito curta!')
else:
    for letra in senha:
        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito = True
        if letra in string.punctuation:
            pontuacao = True

    if maiuscula == False or digito == False or pontuacao == False:
        if maiuscula == False:
            print('Erro! Senha não tem letras maiúsculas.')

        if digito == False:
            print('Erro! Senha não tem dígitos numéricos.')

        if pontuacao == False:
            print('Erro! Senha não tem caracteres especiais.')
    else:
        print('Senha válida!')