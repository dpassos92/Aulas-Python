# Ex039
"""
Crie um programa que com um tuplecom os 20 primeiros classificados do Campeonato Espanhol de Futebol. Depois mostre:
a)Os primeiros 5 classificados.
b)Os últimos 4 classificados.
c)Uma lista com as equipas por ordem alfabética.
d)A posição da equipa Las Palmas.
"""

classificacao = ('Real Madrid', 'Girona', 'Atlético Madrid', 'Barcelona', 'Atlético Bilbao',
                 'Real Sociedad', 'Betis', 'Getafe', 'Valencia', 'Las Palmas', 'Rayo Vallecano',
                'Osasuna', 'Villarreal', 'Mallorca', 'Alaves', 'Sevilla', 'Celta Vigo', 'Cadiz',
                'Granada', 'Almeria')

print(f'Os primeiros 5 classificados são: \n')
for c in classificacao[0:5]:
    print(f'{classificacao.index(c)+1}º {c}')

print(f'\nOs últimos 4 classificados são: \n')
for c in classificacao[-4:]:
    print(f'{classificacao.index(c)+1}º {c}')

print(f'\nA lista das equipas por ordem alfabética: \n')
ordem_alfabetica = sorted(classificacao)
for c in ordem_alfabetica:
    print(f'{c}')

print(f'\nA equipa Las Palmas está na posição: {classificacao.index('Las Palmas')+1}º ')
