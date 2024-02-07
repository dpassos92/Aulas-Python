# Ex050
"""
Melhore o exercício 49, exibindo no final.
a)A soma de todos os valores pares.
b)A soma dos valores da segunda coluna.
c)O maior valor daterceira linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for indice in range(0, 3):
    for valor in range(0, 3):
        matriz[indice][valor] = int(input(f'Digite um valor para [{indice}][{valor}]: '))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f'[ {matriz[indice][valor]} ]', end=' ')
    print()

soma = 0

for indice in range(0, 3):
    for valor in range(0, 3):
        if matriz[indice][valor] % 2 == 0:
            soma += matriz[indice][valor]

print(f'A soma dos números pares é: {soma}')

soma_coluna2 = 0
for indice in range(0, 3):
    if matriz[indice][1]:
        soma_coluna2 += matriz[indice][1]

print(f'A soma dos números na segunda coluna é: {soma_coluna2}')

maior = 0
for indice in range(0, 3):
    for valor in range(0, 3):
        if maior == 0:
            maior = matriz[2][valor]
        if matriz[2][valor] > maior:
            maior = matriz[2][valor]

print(f'O maior número na terceira linha é: {maior}')

'''[1][2][3]
[4][5][6]
[7][8][9]'''

