# EX004
"""
Cria um programa que leia um número introduzido pelo utilizador e que mostre o seu antecessor e sucessor.

"""

num1 = int(input("Digite um número"))
num_antecessor = num1 - 1
num_sucessor = num1 + 1

print("O número antecessor ao digitado é:", num_antecessor)
print("O número sucessor do digitado é:", num_sucessor)