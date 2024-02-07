# Ex040
"""
Crie um programa que gere 5 números aleatórios dentro de um tuple. Depois mostra a listagem de números gerados,
o menor e o maior da lista.
"""

from random import randint

pc = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0,10), randint(0, 10))

for c in pc:
    print(c, end='  ')

print(f'\nO maior numero gerado foi {max(pc)}')
print(f'O menor número gerado foi {min(pc)}')