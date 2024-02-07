# Ex081
"""
Crie uma classe chamada Livro que tenha os atributos: titulo, ano, autor e disponibilidade.
Utilize getters e setters para manipular as propriedades.
"""

class Livro:
    def __init__(self):
        self.__titulo = ''
        self.__ano= 0
        self.__autor= ''
        self.__disponibilidade = False

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def disponibilidade(self):
        if disponibilidade:
            return f'O livro está disponível.'
        else:
            return f'O livro não se enconta disponível'

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade


print('--Biblioteca--')
a = input("Clique ENTER para adicionar um novo livro...")
titulo = input('Titulo: ')
ano = int(input('Ano: '))
autor = input('Autor: ')
disponibilidade = input('Disponibilidade: [s/n] ').strip().lower()

if disponibilidade == 's':
    disponibilidade = True
else:
    disponibilidade = False

livro = Livro()
livro.titulo = titulo
livro.ano = ano
livro.autor = autor

print()
print(livro)

print(f'Titulo: {livro.titulo}')
print(f'Ano de Publicação: {livro.ano}')
print(f'Autor: {livro.autor}')
print(livro.disponibilidade)
