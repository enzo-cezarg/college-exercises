# Declara os conjuntos
a = set([1, 2, 3, 4, 5, 6])
b = set([4, 5, 6, 7, 8, 9])
c = set([1, 3, 5])

# Realiza operações e imprime na tela
print(f'União          a + b: {a.union(b)}')
print(f'Diferença      a - b: {a.difference(b)}')
print(f'Diferença      b - a: {b.difference(a)}')
print(f'Intersecção    a & b: {a.intersection(b)}')
print(f'Dif. simétr.   a ^ b: {a.symmetric_difference(b)}')

print('===='*10)
print(f'a contém c  :     {a.issuperset(c)}')
print(f'c contido em a:   {c.issubset(a)}')