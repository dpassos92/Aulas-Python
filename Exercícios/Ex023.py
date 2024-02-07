# EX023
"""
Faça um programa que mostre a tabuada de um número introduzido pelo utilizador.
"""

# Pedir um número
num = int(input("Digite um número para ver a sua tabuada: \n"))


print(f"Tabuada do {num}: \n")
for c in range(0, 10):
    print(num, "x", c + 1, "=", num * (c + 1))
