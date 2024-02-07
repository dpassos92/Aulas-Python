# EX071
"""
Escreva um programa que peça ao utilizador para inserir dois números e divida o primeiro pelo segundo. Utilize o tratamento de exceções para lidar com casos em que o segundo número é zero e quando a entrada não é um número válido.
"""


def divisao(a, b):
    div = a / b
    return div


try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A divisão de {num1} por {num2} é {divisao(num1, num2):.1f}')

except ValueError:
    print('ERRO! NÃO DIGITOU NENHUM NÚMERO.')

except ZeroDivisionError:
    print('Não é possível dividir por zero')

except Exception as erro:
    print(f'{erro.__class__}')

