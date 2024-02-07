# Ex080
"""
Crie uma classe chamada “Aluno” que possua atributos para armazenar o nome e as notas de um aluno.
Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).
"""


class Aluno:
    def __init__(self, nome, notas):
        self.__nome = nome
        self.__notas = notas

    def get_nome(self):
        return f'O nome do aluno é {self.__nome}'

    '''def set_nome(self, nome):
        self.__nome = nome
        print(f'O novo nome do aluno é {self.__nome}')'''

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        self.__notas = notas

    def calcular_media(self):
        return sum(self.__notas)/len(self.__notas)

    def situacao(self, media):
        if media >= 9.5:
            print(f'O aluno {nome} tem média de {media} está aprovado!!')
        else:
            print(f'O aluno {nome} tem média de {media} está reprovado!!')


nome = input('Digite o nome do aluno: ')

notas = list()
cont = 0
while True:
    nota = float(input(f'Digite a {cont+1}º nota: '))
    cont += 1
    notas.append(nota)
    if cont == 5:
        break

aluno = Aluno(nome, notas)

aluno.get_nome()
aluno.get_notas()
media = aluno.calcular_media()
aluno.situacao(media)
