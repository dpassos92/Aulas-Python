# Ex062
"""
Crie um programa que tenha uma função que receba o nome de um aluno e uma lista das suas notas. Ele deve calcular
a média do aluno e mostrar no ecrã o nome do aluno, a sua média e se ele ficou aprovado ou não.

"""
from time import sleep

#resolução1
'''print('-=-'*10)
print(f'{'Registo de notas':^30}')
print('-=-'*10)'''

'''def conta_notas(aluno, *notas):
    cont = 0
    soma = 0
    lista_notas = list()

    for num in notas:
        soma += num
        cont += 1
        lista_notas.append(num)

    while True:
        continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
        if continuar == 'S':
            num = float(input('Digite a nota: '))
            lista_notas.append(num)
            cont += 1
            soma += num
        if continuar == 'N':
            break

    media = soma / cont

    if media >= 9.5:
        print('-=-'*20)
        print(f'A calcular a média do {aluno}', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        print(f'A média do {aluno} é {media}.')
        sleep(1)
        print('Está aprovado!!!')
        print('-=-' * 20)

    else:
        print('-=-' * 20)
        print(f'A calcular a média do {aluno}', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        print(f'A média do {aluno} é {media}.')
        sleep(1)
        print(f'Está reprovado!!!')
        print('-=-' * 20)


aluno = input('Digite o nome do aluno: ')
num = float(input('Digite a nota: '))
conta_notas(aluno, num)'''


# alternativa

def pauta(nome, lista_notas):
    print('~' * 30)
    print(f'{'Pauta de notas':^30}')
    print('~' * 30)
    sleep(1)
    soma_notas = 0
    for notas in lista_notas:
        soma_notas += notas

    media = soma_notas / len(lista_notas)
    situacao = 'Aprovado' if media >= 9.5 else 'Reprovado'
    sleep(0.5)
    print(f'\nMédia: {media:.2f}')
    sleep(0.5)
    print(f'Situação: {situacao}')


nome = input('Digite o nome do aluno: ')
notas = list()
contador = 0

while True:
    nota = float(input(f'Digite a {contador + 1}º nota: '))
    notas.append(nota)
    contador += 1
    opcao = input('Deseja continuar? [S/N]\n ')
    if opcao == 'N':
        break

pauta(nome, notas)
