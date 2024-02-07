# Ex052
"""
Crie um programa que leia o nome e a média de um aluno, calculando a sua situação, tudo dentro de um dicionário. No final mostre todo o conteúdo do dicionário.
Situação:
Média >= 9,5 –Aprovado
Média < 9,5 -Reprovado
"""

# iniciar dicionário
aluno = dict()

# pedir dados para adicionar às keys
aluno['Nome'] = (input('Digite o nome do aluno: ')).strip()
aluno['Média'] = int(input(f'Digite a média do {aluno['Nome']}: '))
print()

# mostra os dados das que estão em cada key
print(f'Nome: {aluno['Nome']}')
print(f'Média: {aluno['Média']}')

# condição a apresentar para o valor que estiver na média
if aluno['Média'] >= 9.5:
    print(f'APROVADO!!')
else:
    print(f'REPROVADO!!')

