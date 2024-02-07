# Ex057
"""
Melhore o exercício 55 para que permita a entrada de vários jogadores. Defina um sistema de visualização que
permita ao utilizar procurar pelos resultados de um jogador específico.
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
while True:
    escolha = input('Qual o jogador que quer ver as estatísticas: ')
    encontrado = False
    for jogador in jogadores:
        if escolha.lower().strip() == jogador['Nome'].lower().strip():
            print(f"Estatísticas de \033[34m{jogador['Nome']}\033[m:")
            print(f"Jogos: {jogador['Jogos']}")
            print(f"Golos: {jogador['Golos']}")
            print(f"Média de Golos: {jogador['Média de Golos']:.2f}")
            encontrado = True
            print('======'*5)
            break
    if not encontrado:
        print('\033[31mJogador não foi encontrado...\033[m')
    continuar = input('Deseja continuar: [S/N]:').strip().upper()[0]
    if continuar in 'Nn':
        break
    print('======' * 5)