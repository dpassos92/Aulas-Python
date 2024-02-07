# Ex036
"""
Desenvolva o jogo par ou ímpar. O jogo só será interrompido quando o jogador perder e deverá exibir o total de
vitórias consecutivas.
"""

# par ou impar
from random import randint
v = 0

print('-==-' * 10)
print('--==--==--==- \033[35mPAR OU ÍMPAR\033[m -==--==--==--')
print('-==-' * 10)

while True:
    escolha = int(input('Que o valor? '))
    pc = randint(1,10)
    parimpar = input('Par ou Impar: [P/I]').strip().upper()[0]
    soma = escolha + pc
    while parimpar not in 'PpIi':
        print('Opção inválida... tente novamente...')
        parimpar = input('Par ou Impar: [P/I]').strip().upper()[0]
    print('-==-'*15)
    if soma % 2 == 0:
        print(f'Você escolheu o \033[34m{escolha}\033[m e o pc escolheu \033[31m{pc}\033[m. A soma \033[33m{soma} é PAR\033[m')
        if parimpar in 'Pp':
            print('\033[33mGanhou!!\033[m Mais uma ronda...')
            v += 1
            print('-==-' * 15)
        else:
            print('\033[31mPERDEU!!!\033[m')
            print('-==-' * 15)
            break
    if soma % 2 == 1:
        print(f'Você escolheu o \033[34m{escolha}\033[m e o pc escolheu \033[31m{pc}\033[m. A soma \033[33m{soma} é ÍMPAR\033[m')
        if parimpar in 'Ii':
            print('\033[33mGanhou!!\033[m Mais uma ronda...')
            v += 1
            print('-==-' * 15)
        else:
            print('\033[31mPerdeu!!!\033[m')
            print('-==-' * 15)
            break
    print('-==-'*15)
print(f'Você ganhou \033[33m{v}\033[m vezes seguidas!! Bom jogo!!')
print(f'Volte sempre!!')