# EX005
"""Cria um programa que leia 2 valores introduzidos pelo utilizador e que apresente a sua SOMA, SUBTRAÇÃO,
MULTIPLICAÇÃO, DIVISÃO e RESTO.
"""


# Ler números do utilizador
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Estruturar variáveis e calculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

# Apresentar resultados no ecrã
print("\nSoma =", num1, "+", num2, "=", soma)
print("Subtração =", num1, "-", num2, "=", subtracao)
print("Multiplicação =", num1, "*", num2, "=", multiplicacao)
print("Divisão =", num1, "/", num2, "=", divisao)
print("Resto =", num1, "%", num2, "=", resto)