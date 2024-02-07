# Ex045
"""
Crie um programa onde o utilizador insira 5 números dentro de uma lista. Os valores devem ser registados já na
posição correta [ordem crescente] e no final mostre a lista ordenada. Não utilizar o sort()
"""
lista = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if cont == 0:
        lista.append(num)
        print(f'Adicionado na 1 posicao')
    elif num > lista[-1]:
        lista.append(num)
        print(f'Adicionado na última posição')
    else:
        indices = 0
        # vai verificar em todas as posições se o número inserido é menor ou igual ao existente
        while indices <= len(lista):
            if num <= lista[indices]:
                lista.insert(indices, num)
                print(f'Novo número adicionado na posição {indices+1}')
                break
            indices += 1
print(lista)
