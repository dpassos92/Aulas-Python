# Ex078
"""
Crie uma classe chamada “Círculo” que possua um atributo privado para armazenar o raio e métodos getterse setters
para definir o raio, calcular a área e o perímetro do círculo.
"""

import math


class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
        return f'O raio do círculo é {self.__raio}'

    def set_raio(self, raio):
        print(f'O valor do raio passou a ser {raio}')
        self.__raio = raio

    def perimetro(self):
        print(f'O perimetro do círculo é {2 * math.pi * self.__raio}')

    def area(self):
        print(f'A area do cículo é {math.pi * (self.__raio * self.__raio)}')


raio = int(input('Digite o raio do círculo'))
circulo = Circulo(raio)
print(circulo.get_raio())
circulo.perimetro()
circulo.area()

print()

novo_raio = int(input('Digite o raio do círculo'))
circulo.set_raio(novo_raio)
circulo.perimetro()
circulo.area()



