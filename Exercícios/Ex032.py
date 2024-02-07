# EX032
"""Escreva um programa que leia um número N inteiro qualquer e mostre os N primeiros elementos de uma sequência de
Fibonacci.
"""

print('-==-==-\033[33mSequência de Fibonacci\033[m-==-==-')
num = int(input('Digite o número de elementos que quer: '))

n1 = 0
n2 = 1

cont = 3

while num <= 0:
    print('Por favor, insira um número positivo!!')
    num = int(input('Digite o número de elementos que quer: '))
if num == 1:
    print(f'{n1}', end='')
elif num == 2:
    print(f'{n1} -> {n2} ', end='')
else:
    print(f'{n1} -> {n2} ', end='')
    while cont <= num:
        num -= 1
        n3 = n1 + n2
        print(f'-> {n3}', end='')
        # actualizar valores
        n1 = n2
        n2 = n3
print(' -> FIM')

