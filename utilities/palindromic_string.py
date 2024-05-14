stringInput = input('Digite uma palavra para ser verificada: ')

stringReverse = stringInput[::-1]

if stringInput == stringReverse:
    print('Esta palavra é um palíndromo! (Permanece igual quando escrita ao contrário)')
else:
    print('Esta palavra NÃO é um palíndromo! (Não permanece igual quando escrita ao contrário)')