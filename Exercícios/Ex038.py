#Ex038
"""
Crie um programa que leia um número de 0 a 20 introduzido pelo utilizador. Depois deverá mostrar por extenso o
número introduzido.
"""

numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'
                   , 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezaseis', 'dezasete', 'dezoito'
                   , 'dezanove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))

print(numeros_extenso[num])
