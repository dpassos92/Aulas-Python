# Ex054
"""
Crie um simulador de crédito habitação simples e sem taxas, que solicite o nome, ano de nascimento, rendimentos
mensais, despesas mensais, montante do crédito e prazo em anos, guardando tudo dentro de um dicionário. Calcule,
acrescentando ao dicionário, a idade, o remanescente após despesas, quanto deverá pagar mensalmente pelo crédito e se
o crédito foi aprovado sempre que o remanescente seja superior ao valor mensal do crédito.
"""

from datetime import date
from time import sleep

print('=========='*3)
print(f'\033[32m{'Único Banco':^30}\033[m')
print('=========='*3)

# criar dicionário para banco
banco = dict()

# inserir dados no dicionário
banco['Nome'] = input('Nome: ')
banco['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
banco['Rendimento'] = float(input('Rendimentos: '))
banco['Despesas'] = float(input('Despesas: '))
banco['Crédito'] = float(input('Montante do crédito: '))
banco['Prazo'] = int(input('Prazo em anos: '))

# calculos e inserir no dicionário
banco['Idade'] = date.today().year - banco['Ano de Nascimento']
banco['Remanescente'] = banco['Rendimento'] - banco['Despesas']
banco['Mensalidade'] = banco['Crédito'] / (banco['Prazo'] * 12)

print()
print('=========='*3)
print('Analisando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
print()

for k, v in banco.items():
    if k == 'Nome':
        print(f'Cliente: {v}')
    elif k == 'Idade':
        print(f'{k}: {v}')
    elif k == 'Remanescente':
        print(f'Valor {k}: {v}€')

print()
if banco['Remanescente'] > banco['Mensalidade']:
    print(f'\033[32mCrédito Aprovado!!\033[m')
    print(f'A sua mensalidade será de {banco['Mensalidade']:.2f}€')
else:
    print(f'\033[31mCrédito negado!!\033[m')
