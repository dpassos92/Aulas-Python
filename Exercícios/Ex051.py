# EX051
"""
Cria um programa que crie palpites para o Euromilhões. O programa deve perguntar quantas chaves serão geradas e
deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir] e 2 estrelas de 1 a 12 [sem repetir]. Cada sorteio deve
ser guardado numa lista composta.
"""

# importar bibliotecas
from random import randint
from time import sleep
# Apresentação
print('======'*5)
print(f'\033[33m{'Euromilhões':^30}\033[m')
print('======'*5)

sleep(1)
print('Bem vindo ao gerador de chaves do \033[33mEuromilhões!!!\033[m')
sleep(1)
chaves = int(input('\nDigite o número de chaves que quer gerar: '))

# Fazer o programa "pensar"
sleep(1)
print('A gerar chaves.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\n')

# iniciar listas
chaves_geradas = [[], []]
numeros = list()
estrelas = list()

# gerar o número de chaves pedidas....
for cont in range(0, chaves):
    # Gerar número de forma aleatória sem repetir e só aí é que vão para a lista números
    while len(numeros) < 5:
        num = randint(1, 50)
        if num not in numeros:
            numeros.append(num)
    numeros.sort()
    # Gerar estrela de forma aleatória sem repetir e depois vão para a lista estrelas
    while len(estrelas) < 2:
        estrela = (randint(1, 12))
        if estrela not in estrelas:
            estrelas.append(estrela)
    estrelas.sort()

    # passar as listas dos números e das estrelas geradas para a lista chaves_geradas
    chaves_geradas[0] = numeros
    chaves_geradas[1] = estrelas

    # Apresentar as chaves_geradas
    print(f'{cont+1}º Chave --> {chaves_geradas[0]}, *{chaves_geradas[1]}')
    # Limpar a lista para apresentar as chaves seguintes
    chaves_geradas[0].clear()
    chaves_geradas[1].clear()
    print()


