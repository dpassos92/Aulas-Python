# Ex068
"""
Crie um programa com uma função que vai receber várias notas de alunos e vai retornar um dicionário com o seguinte:
a)Quantidade de notas
b)A maior nota
c)A média da turma
d)A situação (lógico opcional)
>12 –boa
<9,5 –fraca
>9,5 e <12 -razoável
"""


def apresentacao():
    print('-=-'*10)
    print(f'{'Situação da Turma':^30}')
    print('-=-'*10)


def sit_turma(lista, situacao=False):
    lista = list()
    lista.append(notas)
    maior = 0
    soma = 0

    print(f'\nForam inseridas {len(lista[0])} notas na turma')

    for v in lista[0]:
        soma += v
        if v > maior:
            maior = v
    print(f'A maior nota da turma foi {maior}\n')

    media = soma / len(lista[0])
    print(f'A média da turma foi {media:.2f}')

    if situacao:
        if media > 12:
            situacao = 'Boa'
            return f'A situação da turma é {situacao}'
        elif media < 9.5:
            situacao = 'Fraca'
            return f'\nA situação da turma é {situacao}'
        elif 9.5 < media < 12:
            situacao = 'Razoável'
            return f'\nA situação da turma é {situacao}'


apresentacao()
notas = [10, 15, 13, 16, 20, 5, 17]
print(sit_turma(notas, situacao=True))
