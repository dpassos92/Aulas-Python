# Ex055
"""
Crie um programa que guarde o aproveitamento de um jogador de futebol. O programa deverá ler o nome, quantos jogos
jogou e a quantidade de golos por jogo e guardar tudo num dicionário. No dicionário, deve calcular a média de golos
por jogo.
"""

jogadores = list()
print('======'*5)
print(f'{"Fantasy Football":^30}')
print('======'*5)
while True:
    jogador = {'Nome': input('Digite o nome do jogador: ').strip(),
               'Jogos': int(input('Número de jogos que participou: ')),
               'Golos': int(input('Número de golos: '))}
    jogador['Média de Golos'] = (jogador['Golos'] / jogador['Jogos'])
    jogadores.append(jogador)
    print('======' * 5)
    continuar = input('Deseja continuar: [S/N]:').strip().upper()[0]
    if continuar in 'Nn':
        break
    print('======' * 5)

print('======'*5)
for jogador in jogadores:
    print(f"Estatísticas de \033[34m{jogador['Nome']}\033[m:")
    print(f"Jogos: {jogador['Jogos']}")
    print(f"Golos: {jogador['Golos']}")
    print(f"Média de Golos: {jogador['Média de Golos']:.2f}")
    print('======'*5)
