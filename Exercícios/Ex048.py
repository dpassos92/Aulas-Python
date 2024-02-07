# Ex048
"""
Crie um programa que leia 10 números introduzidos pelo utilizador e guarde-os numa lista que separe os valores
pares dos ímpares. No final exiba os valores pares e ímpares por ordem crescente.
"""

pares = list()
impares = list()
lista = list()

for c in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

lista.append(pares)
lista.append(impares)

lista[0].sort()
lista[1].sort()

print(lista)
print(f'Os números pares introduzidos foram {lista[0]}')
print(f'Os números impares indroduzidos foram {lista[1]}')


# alterativa
#lista que vai receber os números
numeros = [[], []]

#peço os números e valido se são pares
#se forem pares vão para o indice 0, se forem impares vão para o indice 1
for cont in range(0, 10):
    num = int(input(f'Digite o {cont+1}.º número: '))
    if num % 2 ==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

# ordeno cada lista dentro da lista números
numeros[0].sort()
numeros [1].sort()

print(f'Os números digitados são {numeros}')
print(f'Os números pares por ordem são: {numeros[0]}')
print(f'Os números impares por ordem são: {numeros[1]}')

