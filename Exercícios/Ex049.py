# Ex049
"""
Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz com a
formatação adequada.
"""

valor = list()
matriz = list()

for i in range(0, 3):
    for v in range(0, 3):
        num = int(input(f'Digite um número para a posição [{i}][{v}]'))
        valor.append(num)
    matriz.append(valor[:])
    valor.clear()


for i in range(0, len(matriz)):
    for valor in range(0, len(matriz[0])):
        print(f'[{matriz[i][valor]}]', end='')
    print()


# alternativa
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for indice in range(0, 3):
    for valor in range(0, 3):
        matriz[indice][valor] = int(input(f'Digite um valor para [{indice}][{valor}]: '))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f'[ {matriz[indice][valor]} ]', end=' ')
    print()
