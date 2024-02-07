# Ex084
"""
Desenvolva uma classe Temperatura que armazene a temperatura em graus Celsius como um atributo privado.
Implemente um getter e um setter usando property para permitir que a temperatura seja ajustada e lida em Celsius,
 e adicione métodos para converter a temperatura para Fahrenheit e Kelvin.
"""


def main():
    opcao = input('Deseja converter para ºKelvin [K] ou para ºFahrenheit [F]').strip().upper()
    while True:
        if opcao == 'K':
            print(temperatura.kelvin(valor))
            break
        elif opcao == 'F':
            print(temperatura.fahrenheit(valor))
            break
        else:
            print('Opção inválida tente novamente....')
            opcao = input('Deseja converter para ºKelvin [K] ou para ºFahrenheit [F]').strip().upper()


class Temperatura:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        self.__temperatura = temperatura

    def fahrenheit(self, temperatura):
        fahrenheit = (temperatura * 1.8) + 32
        self.__temperatura = fahrenheit
        return f'A temperatura {temperatura}ºC convertida em Fahrenheit é {self.__temperatura:.1f}ºF'

    def kelvin(self, temperatura):
        kelvin = (temperatura + 273.15)
        self.__temperatura = kelvin
        return f'A temperatura {temperatura}ºC convertida em Kelvin é {self.__temperatura:.2f}ºK'


valor = float(input('Digite a temperatura em ºC: '))
temperatura = Temperatura(valor)

main()
