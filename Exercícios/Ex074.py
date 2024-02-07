# Ex074
"""
Crie uma classe chamada Livro que tenha dois atributos: titulo e autor. Instancie três objeto dessa classe e
imprima os valores dos atributos.
"""


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro1 = Livro("Hobbit", "Tolkien")
livro2 = Livro("Senhor dos Aneis", "Tolkien")
livro3 = Livro("IT", "Stephen King")

print(f'O livro {livro1.titulo} tem como autor o {livro1.autor}')
print(f'O livro {livro2.titulo} tem como autor o {livro2.autor}')
print(f'O livro {livro3.titulo} tem como autor o {livro3.autor}')
