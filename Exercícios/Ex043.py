# Ex043
"""
Crie um programa que leia 5 números e guarde-os numa lista. No final mostre o maior e o menor valor e a respetiva
posição na lista.
"""

lista = list()
maior = 0
menor = 0
pos_maior = 0
pos_menor = 0

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
    if maior == menor == 0:
        maior = num
        pos_maior = lista.index(num)
        menor = num
        pos_menor = lista.index(num)
    elif num > maior:
        maior = num
        pos_maior = lista.index(num)
    elif num < menor:
        menor = num
        pos_menor = lista.index(num)

print(f'O maior número registado foi o {maior}, na posição {pos_maior} do index')
print(f'O menor número registado foi o {menor}, na posição {pos_menor} do index')
