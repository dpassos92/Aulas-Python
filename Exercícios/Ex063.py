# Ex063
"""
Crie um programa que tenha uma função que receba um número inteiro e mostre a tabuada desse número.
"""

print('-=-'*10)
print(f'{'Tabuada':^30}')
print('-=-'*10)


def tabuada(num):
    print(f'-=-' * 10)
    print(f'Tabuada do {num}')
    for c in range(1, 11):
        multiplicacao = c * n
        print(f'{num} x {c} = {multiplicacao}')
    print(f'-=-' * 10)


while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    tabuada(n)
    continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    print(f'-=-' * 10)
    if continuar in 'Nn':
        break
print('FIM')
