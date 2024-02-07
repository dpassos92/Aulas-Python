# EX053
"""
Crie um programa que sorteie a ordem de jogada num jogo ao “atirar um dado ao ar”. Cada jogador terá um número
aleatório associado dentro de um dicionário. No final ordene o ranking para ver a ordem de jogada.
"""

from random import randint
import operator

# criar dicionário, a key vai ser o nome e o valor vai ser gerado aleatóriamente
jogada = {'Ricardo': randint(1, 6),
          'Diogo': randint(1, 6),
          'Julia': randint(1, 6),
          'Pedro': randint(1, 6)}

# mostrar o resultado da jogada...
for k, v in jogada.items():
    print(f'O jogador {k} tirou {v}')

# coloquei o dicionário jogadas dentro da lista ordem,
# fui buscar o item que estaria no index 1, neste caso é o valor gerado
# e inverti a ordem dos resultados do maior para o menor
ordem = list(sorted(jogada.items(), key=operator.itemgetter(1), reverse=True))

# apresentar os resultados
print()
print('=====' * 7)
print(f'A ordem dos jogadores é:')

# iniciar contador
cont = 0

while cont < len(ordem):
    for k, v in ordem:
        print(f'{cont + 1}º é o jogador {k} pois tirou {v}')
        cont += 1
