#Ex037
"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa registada o programa deverá perguntar se o utilizador quer continuar ou não. No final mostre:
a)Quantas pessoas têm mais de 25 anos.
b)Quantos homens com menos 17 anos foram registados.
c)Quantas mulheres foram registadas.
d)Quantos menores de idade foram registados.
"""

print('-==-' * 9)
print('--==- \033[35mRegisto de Utilizadores\033[m -==--')
print('-==-' * 9)

from time import sleep

mais25 = 0
h_menos17 = 0
mulher = 0
menores = 0
continuar = ' '

while True:
    sexo = input('SEXO: [M/F] ').strip().upper()[0]
    while sexo not in 'MmFf':
        print('OPÇÃO INVÁLIDA!!! Tente novamente...')
        print('-==-' * 10)
        sexo = input('SEXO: [M/F] ').strip().upper()[0]
    idade = int(input('IDADE: '))
    while idade <= 0:
        print('OPÇÃO INVÁLIDA!!! Tente novamente...')
        print('-==-' * 10)
        idade = int(input('IDADE: '))
    if idade >= 25:
        mais25 += 1
    if sexo in 'Mm' and idade < 17:
        h_menos17 += 1
    if sexo in 'Ff':
        mulher += 1
    if idade < 18:
        menores += 1
    continuar = input('Continuar a registar? [S/N] ').strip().upper()[0]
    while continuar not in 'SsNn':
        print('OPÇÃO INVÁLIDA!!! Tente novamente...')
        continuar = input('Continuar a registar? [S/N] ').strip().upper()[0]
    if continuar in 'Nn':
        print('-==-' * 10)
        print('A analisar registos...')
        print('-==-' * 10)
        sleep(1)
        break
    print('-==-' * 10)
print(f'Ao todos foram registadas {mais25} pessoas com mais de 25 anos.')
print(f'Foram também registados {h_menos17} homens com menos de 17 anos.')
print(f'Foram registadas {mulher} mulheres ao todo.')
print(f'Tivemos ainda {menores} menores registados.')
print('FIM')