# EX006
"""
Cria um programa que leia 5 notas introduzidas pelo utilizador e que calcule a média aritmética entre eles.
"""

# Inserir 5 notas para cálcular a média
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))
nota5 = float(input("Digite a quinta nota:"))

#calcular a média
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#exibir a nota
print("\nA sua média final é:", media)