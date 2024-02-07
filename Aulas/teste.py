'''nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o seu ano de Nascimento: "))
ano_actual = 2023
idade = ano_actual - ano_nascimento

print("Olá", nome, "seja bem-vindo(a) ao nosso programa")
print("Vejo que tem", idade, "anos de idade.")'''

'''# ex
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

texto = "Feliz Ano Novo!"
lingua = "pt-pt"

ler = gTTS(text=texto, lang=lingua)

ler.save("leitura.mp3")

os.system("leitura.mp3")'''

# variáveis compostas
# Os tuples são IMUTÁVEIS depois de declarados (usam parentises ())
'''estante = ('PLaystation', 'Xbox', 'Nintendo', 'Gameboy')
print(estante[0])'''

'''estante = ('PLaystation', 'Xbox', 'Nintendo', 'Gameboy')
for consola in estante:
    print(consola)

print(estante.index('Xbox') +1)'''

'''estante = ('PLaystation', 'Xbox', 'Nintendo', 'Gameboy')
estante_ordem_alfabetica = sorted(estante)'''

'''print(estante_ordem_alfabetica)'''

'''# as listas são mutáveis e são usados [] para declarar
estante = ['PLaystation', 'Xbox', 'Nintendo', 'Gameboy']
estante.append('Sega')
estante.insert(0, 'Sega')
estante.remove('Sega')
estante.pop(3) # elimina consoante o index
del estante[3]
estante.pop() # elimina apenas o último'''

'''numeros = [1,2,4,6,7,8]
numeros.sort()
numeros.sort(reverse=True) #inverte a ordem dos números'''

# LISTAS
'''lista = list()
tupla = tuple()

tupla_um = (2,3,4,5)
tupla_dois = (6,5,4,3)

soma_tuple = tupla_um + tupla_dois

print(soma_tuple)'''

'''lista = [2,3,4,5]
nova_lista = lista[:] # com o [:] vai fazer uma cópia dos elementos para a nova lista

nova_lista[0] = 7 #vai alterar nas duas listas

print(f'Esta é a lista principal: {lista}')
print(f'Esta é a lista secundária: {nova_lista}')

for v in lista:
    print(v)

print(f'No indice 0 está o 2')
print(f'No indice 1 está o 3')
print(f'No indice 2 está o 4')
print(f'No indice 3 está o 5')

for i, v in enumerate(lista): # primeira variável guarda o indice e o segundo o valor
    print(f'Na posiçao {i} está o valor {v}')'''

'''lista = list()

for cont in range(0, 5):
    lista.append(int(input('Digite um número: ')))'''

'''for cont in range(0, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
    print(f'O número {num} foi adicionado com sucesso')

lista.pop(0)

for valor in lista:
    print('\n', valor, end=' ')'''

# listas 2
'''aluno = list()

aluno.append('Diogo')
aluno.append(31)

turma = list()
turma.append(aluno)

aluno[0] = 'Amanda'
aluno[1] = 30

print(aluno)
print(turma)'''

'''turma = list()
aluno = list()

for c in range(0, 3):
    aluno.append(input('Digite o nome do aluno: '))
    aluno.append(int(input('Digite a idade: ')))
    turma.append(aluno[:])
    aluno.clear()
'''

'''for aluno in turma:
    print(f'O aluno {aluno[0]} tem {aluno[1]} anos.')'''

'''for i, a in enumerate(turma):
    print(f'O {i+1}º aluno é {a}')'''

'''for i in range(0, len(turma)):
    for aluno in range(0, len(turma[0])):
        print(f'{i+1}.º ---> {turma[i][aluno]}')
'''

# Dicionários
'''aluno = {'Nome': 'Cesar', 'Média': 14}

print(aluno['Nome'])
print(f'O aluno {aluno['Nome']} tem a média de {aluno['Média']}')

if aluno['Média'] >= 9.5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno['Situação'])

print(aluno.items())
'''

'''aluno = dict()

aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Ex001'] = int(input('Digite a nota do Ex001: '))
aluno['Ex002'] = int(input('Digite a nota do Ex002: '))
aluno['Ex003'] = int(input('Digite a nota do Ex003: '))

print(aluno.items())

aluno['Média'] = (aluno['Ex001'] + aluno['Ex002'] + aluno['Ex003']) / 3
print(aluno.items())
del aluno['Média']
print(aluno.items())'''

'''cidade = {'Nome': 'Porto', 'Código': 'OPO', 'Baixa': 'Ribeira', 'Rio': 'Douro'}
cidade2 = {'Nome': 'Lisboa', 'Código': 'LX', 'Baixa': 'Chiado', 'Rio': 'Tejo'}

pais = list()

pais.append(cidade)
pais.append(cidade2)
print(pais)'''

'''for elemento in cidade.values():
    print(elemento)

for elemento in cidade.keys():
    print(elemento)

for elemento in cidade.items():
    print(elemento)

for k, v in cidade.items():
    print(f'O {k} é {v}')'''

'''cidade = {'Nome': 'Porto', 'Código': 'OPO', 'Baixa': 'Ribeira', 'Rio': 'Douro'}
cidade2 = {'Nome': 'Lisboa', 'Código': 'LX', 'Baixa': 'Chiado', 'Rio': 'Tejo'}

pais = list()

pais.append(cidade)
pais.append(cidade2)

for c in range(0, len(pais)):
    print(f'Cidade: {pais[c]['Nome']} ----> Registada')'''

# Rotinas e funções
# import

'''# Definir Funções
def insere_linha():
    print('-=-=-=-=-=-=-=-=-=-=-=')


#programa principal
print('Código com prints')
print('-=-=-=-=-=-=-=-=-=-=-=')
print('Olá Mundo!')
print('-=-=-=-=-=-=-=-=-=-=-=')


print()
print('Código com função')
insere_linha()
print('Olá Mundo!')
insere_linha()
insere_linha()'''


'''def cabecalho(msg):
    print('~~~~~~~~~~~~~~~~~~~~')
    print(msg)
    print('~~~~~~~~~~~~~~~~~~~~')
    print()


def soma(a, b):
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


def conta_numeros(*num):
    print(f'Inseriu {len(num)} números')
    for numeros in num:
        print(f'{numeros}', end=' ')
    print()


# Programa Principal
cabecalho('Mundo das funções!!')
print('Função Soma')
soma(2, 5)
soma(4, 4)
soma(13, 15)
print()
print('Função Desempacotar')
conta_numeros(1, 2, 3, 4, 5, 6)
conta_numeros(1, 3, 5)
conta_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)'''
