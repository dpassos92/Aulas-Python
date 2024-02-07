# Ex076
"""
Crie uma classe Produto com os atributos nome e quantidade em stock. Adicione um método que mostre o stock no
estilo “O produto X tem Y unidades em stock”. Adicione um novo método que aumenta a quantidade de stock numa
determinada quantidade.
"""


class Produtos:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def stock(self):
        print(f'O produto {self.nome} tem {self.quantidade} unidades em stock.')

    def stock_plus(self, valor):
        self.quantidade += valor


produto1 = Produtos("Lapis", 120)
produto2 = Produtos("Caneta", 50)

produto1.stock()
produto2.stock()

produto1.stock_plus(20)
produto2.stock_plus(100)

produto1.stock()
produto2.stock()

