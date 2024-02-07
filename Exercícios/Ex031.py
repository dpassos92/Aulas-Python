# Ex031
"""
Desenvolva um programa que leia um número qualquer e que mostre o seu fatorial.
"""

f = int(input('Digite o valor para saber o seu FACTORIAL: '))

num = f
factorial = 1

print(f'{f}! = ', end= '')
for c in range(1, f + 1):
    factorial *= num
    num -= 1
    if num > 0:
        print(f'{num+1} * ', end='')
    else:
        print(f'{num+1} ', end='')
print(f'= {factorial}')


'''# Maneira facil
from math import factorial
# ler número
num = int(input('Digite um número para ver o seu factorial: '))
f = factorial(num)

print(f'O factorial de {num} é {f}')'''

'''#
num = int(input('Digite o valor para saber o seu FACTORIAL: '))

c = num

f = 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= num
    c -= 1
print(f'{f}')'''