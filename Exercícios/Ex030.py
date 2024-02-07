# Ex030
"""
Desenvolva um programa que leia 3 valores e mostre o menu:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
O programa deve realizar a operação solicitada em cada caso.
"""

# iniciar variáveis
menu = 0
maior = 0

# pedir valores
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

#iniciar repetição do menu
while menu != 5:
    print('-=-'*5)
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('-=-'*5)
    # Pedir input para o menu
    menu = int(input('QUAL A SUA OPÇÃO? '))
    # iniciar resposta dada à variavel menu
    if menu == 1:
        soma = num1 + num2 + num3
        print(f'SOMA: {num1} + {num2} + {num3} = {soma}')
    if menu == 2:
        multiplicacao = num1 * num2 * num3
        print(f'MULTIPLICAÇÃO: {num1} * {num2} * {num3} = {multiplicacao}')
    if menu == 3:
        if num1 < num2 and num2 > num3: # posso usar a função max(num1, num2, num3
            maior = num2
            print(f'O maior valor é o {num2}')
        elif num2 < num1 and num1 > num3:
            maior = num1
            print(f'O maior valor é o {num1}')
        elif num1 < num3 and num3 > num2:
            maior = num3
            print(f'O maior valor é o {num3}')
        elif num1 == num2 == num3:
            print('Os três valores são iguais')
    # Pedir novas variáveis
    if menu == 4:
        print('-=-'*5)
        print('NOVOS VALORES')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        num3 = int(input('Terceiro valor: '))
    # Terminar o programa
    if menu == 5:
        print('\n\033[31mENCERRANDO...\033[m')
        break
    if menu > 5:
        print('\033[31mRESPOSTA INVÁLIDA... TENTE NOVAMENTE\033[m')
    print(f'\nProxima operação...')
print('\033[31mPROGRAMA TERMINADO!! Tenha um bom dia!!!\033[m')
