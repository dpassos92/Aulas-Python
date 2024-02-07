# Ex075
"""
Adicione um método à classe desenvolvida no exercício anterior Livro que imprime uma descrição do livro no formato:
“O livro com o titulo X foi escrito pelo autor Y".
"""
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def imprimir(self):
        print(f"O livro {self.titulo} foi escrito pelo autor {self.autor}")


livro1 = Livro("Hobbit", "Tolkien")
livro2 = Livro("Senhor dos Aneis", "Tolkien")
livro3 = Livro("IT", "Stephen King")

livro1.imprimir()
livro2.imprimir()
livro3.imprimir()
