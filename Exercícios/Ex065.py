# Ex065
"""
Crie um programa que tenha uma função que vai receber como parâmetro o ano de nascimento de uma pessoa e que retorne se a pessoa já pode tirar a carta de condução, se precisa de autorização do encarregado de educação ou se não pode.
+18 anos –pode
-16 anos –não pode
-18 e +16 –com autorização
"""

from datetime import datetime

#Resolução1
'''
def validador_carta(ano):
    """
    ->
    :param ano:
    :return:
    """
    v = datetime.today().year - ano
    if v > 18:
        print(f'Você tem {v} anos, já pode tirar a carta!')
    elif v < 16:
        print(f'Você tem {v} anos, ainda não pode tirar a carta!')
    elif 16 <= v <= 18:
        print(f'Você tem {v} anos, pode tirar a carta com autorização!')


ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print()
validador_carta(ano_nascimento)'''


# alternativa
def validador_carta(ano):
    ano_actual = datetime.now().year
    idade = ano_actual - ano
    if idade > 18:
        return f'Com {idade} anos, o cidadão pode tirar a carta de condução.'
    if idade < 16:
        return f'Com {idade} anos, o cidadão não pode tirar a carta de condução.'
    else:
        return f'Com {idade} anos, o cidadão necessita de autoriração para tirar a carta de condução'


ano_nascimento = int(input('Digite o ano de nascimento do cidadão: '))
print(validador_carta(ano_nascimento))
