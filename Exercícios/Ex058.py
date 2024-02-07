# Ex058
"""
Crie um programa que tenha uma função chamada area() que receba as dimensões de um terreno e mostre a área do terreno.
"""


def area(comprimento, largura):
    a = comprimento * largura
    print()
    print(f'A área do terreno é {a}m2')


# código principal
area(largura=int(input('Digite a largura: ')), comprimento=int(input('Digite o comprimento: ')))

# alternativa
largura = int(input('Digite a largura: '))
comprimento = int(input('Digite o comprimento: '))
area(largura, comprimento)
