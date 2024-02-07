# Ex082
"""
Crie uma classe chamada Produto que inclua atributos para o nome e a quantidade em stock.
Utilize a property para aceder a quantidade em stock, garantindo que ela nunca seja negativa.
Inclua um método mostrar_stock que exibe uma mensagem indicando quantas unidades do produto estão disponíveis.
Adicione também um método adicionar_stock que permite aumentar a quantidade de stock de um produto.
"""

class Produto:
    def __init__(self, nome, quantidade_stock):
        self.__nome = nome
        self.__quantidade_stock = quantidade_stock

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def quantidade_stock(self):
        return self.__quantidade_stock

    @quantidade_stock.setter
    def quantidade_stock(self, quantidade_stock):
        if quantidade_stock < 0:
            self.__quantidade_stock = (quantidade_stock * -1)
        else:
            self.__quantidade_stock = quantidade_stock

    def mostrar_stock(self):
        return f'O produto {self.__nome} tem {self.__quantidade_stock} unidades em stock.'

    def adicionar_stock(self, valor):
        if valor < 0:
            self.__quantidade_stock += (valor * -1)
            return f'{valor * -1} unidades adicionadas ao stock de {self.__nome}'
        else:
            self.__quantidade_stock += valor
            return f'{valor} unidades adicionadas ao stock de {self.__nome}'


nome = input('Digite o produto: ').strip().capitalize()
quantidade_stock = int(input('Digite a quantidade em stock do produto: '))

produto = Produto(nome, quantidade_stock)

print(produto.mostrar_stock())
print()
valor = int(input('Digite a quantidade de stock que quer adicionar ao produto: '))
print(produto.adicionar_stock(valor))
print()
print(produto.mostrar_stock())
