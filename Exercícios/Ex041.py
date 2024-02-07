# Ex041
"""
Crie um programa que leia 4 valores e guarde-os num tuple. No final exiba:
a)Quantas vezes aparece o número 7.
b)Em que posição foi digitado o número 5.
c)Quais são os números pares.
O programa deve informar quando não encontrar resposta.
"""

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
num4 = int(input('Digite um valor: '))

numeros = (num1, num2, num3, num4)


print(f'\nO número 7 aparece {numeros.count(7)} vezes.')
if numeros.count(5) >= 1:
    print(f'O número 5 foi digitado na posição {numeros.index(5)+1}')
else:
    print('O número 5 não foi digitado...')

print(f'Números pares digitados: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' -> ')
print('FIM')
