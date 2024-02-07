# Ex059
"""
Crie um programa que tenha uma função que receba um texto como parâmetro e que mostre uma mensagem com tamanho adaptável.
Ex:mostre(“Olá mundo.”)
Saída:
-=-=-=-=-=-=-=-=
   Olá mundo.
-=-=-=-=-=-=-=-=
"""


def mensagem(msg):
    print(f'{'~'*(len(msg) + 6):^30}')
    print(f'{msg:^30}')
    print(f'{'~'*(len(msg) + 6):^30}')


msg = input('Digite a mensagem de boas vindas: ')
mensagem(msg)
