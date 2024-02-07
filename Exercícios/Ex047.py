# Ex047
"""
Crie um programa onde o utilizador possa inserir uma equação matemática que use parênteses. O programa deverá analisar a equação e dizer se a equação tem os parênteses corretos ou se está errado.
((a+b)-c(c/d) ((a+b)-c(c/d))
"""

'''
while True:
    equacao = input('Digite a sua equação: ').strip()
    parentises = equacao.count('(') + equacao.count(')')
    if parentises == 0 or parentises % 2 == 0:
        print(f'A equação {equacao} está correcta')
    elif parentises % 2 == 1:
        print(f'A equação {equacao}, não está correcta...')
    continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
    if continuar in 'Nn':
        break
'''

# alternativa com listas
lista = list()
parentises = 0

while True:
    equacao = input('Digite a sua equação: ').strip()

    for letras in equacao:
        lista.append(letras)

    for letras in lista:
        if letras == "(" or letras == ')':
            parentises += 1

    if parentises % 2 == 0:
        print(f'A equação {equacao} está correcta')
    else:
        print(f'A equação {equacao}, não está correcta...')

    continuar = input('Deseja continuar: [S/N] ').strip().upper()[0]
    if continuar in 'Nn':
        break
print('FIM')