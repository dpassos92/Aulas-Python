# Ex034
"""Crie um programa que leia várias notas introduzidas pelo utilizador. No final mostre quantas notas o utilizador
inseriu, qual a média entre elas e qual a maior e a menor nota.
"""

#iniciar variáveis
cont = 0
maior = 0
menor = 0
soma = 0
continuar = ' '

while True:
    num = float(input('Digite uma nota: '))
    cont += 1
    soma += num
    if maior == menor == 0:
        maior = num
        menor = num
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

    continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
    while continuar not in 'SsNn':
        print('Resposta inválida... Tente novamente')
        continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
    if continuar in 'Nn':
        break
media = soma / cont
print('-=-'*10)
print('A fazer os cálculos finais...')
print(f'Você digitou {cont} notas e a média foi {media:.2f}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
print(f'\033[31mFIM\033[m')
