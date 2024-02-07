# Ex064
"""
Crie um programa que tenha uma função que converta a temperatura de Celsius para Fahrenheit.
"""


def fahrenheit(celsius):
    f = (celsius * 1.8) + 32
    print(f'A temperatura {temperatura}ºC convertida para fahrenheit é {f}ºF')


temperatura = float(input('Digite a temperatura em ºC: '))
fahrenheit(temperatura)
