# Ex044
"""
Crie um programa onde o utilizador possa digitar vários números e guardá-los numa lista. Caso o número inserido
esteja na lista ele não deve ser adicionado. No final mostre todos os valores por ordem DECRESCENTE.
"""

lista = list()

while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Número já se encontra na lista...')
    else:
        lista.append(num)
    continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
    if continuar in 'Nn':
        break

lista.sort(reverse=True)

print('A ordem decrescente dos valores inseridos é: ', end='')
for valor in lista:
    print(valor, end=' > ')
print('FIM')
