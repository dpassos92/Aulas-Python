#Ex033
"""
Crie um programa que leia vários números inteiros e que termine apenas quando o utilizador digitar a opção para
parar. No final mostre quantos números o utilizador inseriu e qual a soma entre eles.
"""

# iniciar variáveis
soma = 0
cont = 0
parar = ' '

#corre programa enquanto a resposta for Sim
while parar not in 'Nn':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    parar = input('Deseja continuar: [S/N]').strip().upper()[0]
    # Enquanto uma resposta válida não for dada, não vai sair deste loop
    while parar not in 'SsNn':
        print('Resposta inválida... tente novamente')
        parar = input('Deseja continuar: [S/N]').strip().upper()[0]
# apresenta os calculos finais
print('-=-'*10)
print('A fazer os calculos finais....')
print(f'Você digitou \033[36m{cont}\033[m números e a sua soma deu \033[36m{soma}\033[m')


'''# alternativa
# iniciar variáveis
soma = 0
cont = 0

# Pedir um número
num = int(input('Digite um valor [0 para parar]: '))

# corre programa enquanto a resposta for Sim
while num != 0:
    soma += num
    cont += 1
    num = int(input('Digite um valor [0 para parar]: '))
# apresenta os calculos finais
print('-=-'*10)
print('A fazer os calculos finais....')
print(f'Você digitou \033[36m{cont}\033[m números e a sua soma deu \033[36m{soma}\033[m')'''