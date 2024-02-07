# EX024
"""
Faça um programa que leia um número inteiro e diga
"""

#Pedir um número e verificar se é número primo
num = int(input("Digite um número: \n"))

#Para sabermos se um número é primo temos que saber a sua raiz quadrada e dividir por todos os números menores que a sua raiz quadrada
raiz_quadrada = int(num ** 0.5)

# Verificar se o número é maior que 1, pois números menores que 2 não são primos
if num > 1:
    #Loop para verificar se o número é divisível por algum número de 2 até a raiz quadrada do número
    for c in range(2, raiz_quadrada + 1):
        if num % c == 0:
            print("Não é número primo")
            #Se o loop for concluído sem ser interrompido pelo break, o bloco de código dentro do else é executado
            break
    else:
        print("É um número primo")
else:
    print("Não é um número primo")


'''#alternativa
#Pedir um número e verificar se é número primo
num = int(input("Digite um número: \n"))
tot = 0

for c in range (1, num +1):
    if num % c == 0:
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[33m", end="")

if tot == 2:
    print(f"O númmero {num} é PRIMO, foi divisível {tot} vezes.")
else:
    print(f"O número {num} não é primo, foi divisivel {tot} vezes.")'''