# Ex061
"""Crie um programa que tenha uma função que receba vários parâmetros como valores inteiros. O programa deve analisar
todos os valores e dizer qual deles é o maior.
"""


def maior(*num):
    resposta = 0
    continuar = 0
    m = 0
    while True:
        respostas = int(input('Digite um número: '))
        continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
        if m == 0:
            m = respostas
        elif respostas >= m:
            m = respostas
        if continuar == 'N':
            break
    print(m)


maior()
