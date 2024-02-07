# Ex042
"""
Crie um programa que tenha um tuplecom nomes de jogos e os seus respetivos preços em sequência.
No final, mostre uma listagem de preços organizados como tabela.
"""

print('------'*5)
print(f'{'Listagem de Preços':^30}')
print('------'*5)

# defini tudo dentro da mesma tupla, podemos ter vários valores em cada index.
jogos_e_precos = (('Baldurs Gate 3', 59.99),
                  ('ELDEN RING', 35.99),
                  ('Cyberpunk 2077', 29.99),
                  ('Lethal Company', 9.75),
                  ('Monster Hunter: World', 15.99),
                  ('Hogwarts Legacy', 25.99),
                  ('Red Dead Redemption 2', 19.79))

# criar variáveis para cada valor dentro de cada index (neste caso temos o nome e o preço)
for jogos, preco in jogos_e_precos:
    pontos = '.' * (30 - len(jogos))
    print(f'{jogos}{pontos} {preco:>5}€')

'''#alternativa
for pos in range(0, len(jogos_e_precos)):
    if pos % 2 == 0:
        print(f'{jogos_e_precos[pos]:-<45}', end=' ')
    else:
        print(f'{jogos_e_precos[pos]:>7.2f}€')'''
