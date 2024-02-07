# Rotinas e funções
# import

'''# Definir Funções
def insere_linha():
    print('-=-=-=-=-=-=-=-=-=-=-=')


#programa principal
print('Código com prints')
print('-=-=-=-=-=-=-=-=-=-=-=')
print('Olá Mundo!')
print('-=-=-=-=-=-=-=-=-=-=-=')


print()
print('Código com função')
insere_linha()
print('Olá Mundo!')
insere_linha()
insere_linha()'''

'''def cabecalho(msg):
    print('~~~~~~~~~~~~~~~~~~~~')
    print(msg)
    print('~~~~~~~~~~~~~~~~~~~~')
    print()


def soma(a, b):
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


def conta_numeros(*num):
    print(f'Inseriu {len(num)} números')
    for numeros in num:
        print(f'{numeros}', end=' ')
    print()


# Programa Principal
cabecalho('Mundo das funções!!')
print('Função Soma')
soma(2, 5)
soma(4, 4)
soma(13, 15)
print()
print('Função Desempacotar')
conta_numeros(1, 2, 3, 4, 5, 6)
conta_numeros(1, 3, 5)
conta_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)'''

# funções2
'''help(print)

primeira = 'Olá'
segunda = 'Mundo'
print(primeira, segunda, sep='_', end=' Terminou')
'''
'''import random

help(random)'''

'''
def soma(a, b):
    """
    -> Esta função imprime no ecrã a soma entre as variáveis.
    :param a: primeiro número da soma
    :param b: segundo número da soma
    :return: sem retorno
    """
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


soma(10, 15)
print('~'*10)
print('Utilizar help')
help(soma)
'''

'''
def escopo(b):
    global a
    a = 8
    b += 5
    c = 3
    print(f'A dentro de vale {a}')
    print(f'B dentro de vale {b}')
    print(f'C dentro de vale {c}')


a = 6
escopo(a)
print(f'A fora vale {a}')'''


def soma(a=0, b=0, c=0):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    s = a + b + c
    '''return s'''
    return f'A soma vale {s}'


resultado = soma(1, 2, 3)
resultado2 = soma(75, 45, 52)
'''print(f'A primeira soma vale {resultado} e a segunda vale {resultado2}')'''
print(resultado)