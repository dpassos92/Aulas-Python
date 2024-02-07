# Ex046
"""
Crie um programa que leia vários números e coloca-os numa lista. Crie duas listas adicionais que vão conter os
números pares e impares da lista principal. No final mostre todas as listas.
"""

lista = list()
lista_pares = list()
lista_impar = list()

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)
    continuar = input('Deseja continuar: [S/N] ')
    if continuar in 'Nn':
        break

print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {lista_pares}')
print(f'Os números ímpares digitados foram: {lista_impar}')
