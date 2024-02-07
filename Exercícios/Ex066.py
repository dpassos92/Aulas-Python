# Ex066
"""
Crie um programa com uma função chamada fatorial(), que receba dois parâmetros: o primeiro será o número a
calcular o fatorial e o segundo será opcional e lógico que indique se será exibido no ecrã ou não o processo de
cálculo do fatorial.
"""


def fatorial(num, mostar=False):
    fat = 1
    for i in range(num, 0, -1):
        if mostar:
            if i == 1:
                print(f'{i} =', end='')
            else:
                print(f'{i} x ', end='')
        fat *= i
    return fat


numero = int(input('Digite um número: '))
opcao = input('Deseja ver o processo? [S/N]\n--->').strip().lower()
mostra = True if opcao == 's' else False
resultado = fatorial(numero, mostra)
print(resultado)
