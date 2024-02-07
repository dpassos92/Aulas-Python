# Ex067
"""Crie um programa com uma função que vai funcionar como a função input(), no entanto vai fazer a validação para
aceitar apenas um valor numérico."""


def validador_numero():
    """

    :return:
    """
    while True:
        numero = (input('Digite um número: '))
        if numero.isnumeric():
            return f'É um valor inteiro.'
        else:
            print(f'Não é um valor numérico, tente novamente')


print(validador_numero())
