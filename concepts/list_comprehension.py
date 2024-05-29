# Inicialização da lista de exemplo
lista = [1, 2 , 3, 4, 5]

# quadrados receberá item^2 para cada item dentro de lista
quadrados = [item ** 2 for item in lista]
print(quadrados)

# quadrados2 receberá item^2 para cada item dentro de lista SE o item for um número par
quadrados2 = [item ** 2 for item in lista if item%2==0]
print(quadrados2)