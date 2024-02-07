# Ex060
"""
Crie um programa que tenha uma função que receba 3 parâmetros: inicio, fim e passo. O programa deve realizar 3 contagens através da função.
a)De 1 até 20, de 2 em 2
b)De 10 até 0, de 1 em 1
c)Contagem personalizada
"""

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    sleep(1)
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            cont += passo
            sleep(0.3)
    else:
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            cont -= passo
            sleep(0.3)
    print('FIM')


contador(1, 20, 2)
contador(10, 0, 1)
print()
print(f'~' * 20)
print('Chegou a hora de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
