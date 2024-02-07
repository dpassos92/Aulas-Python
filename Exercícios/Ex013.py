# EX013
"""
Crie um programa que leia uma palavra de 6 letras e que a escreva ao contrário.
Ex:
palavra = “Python”
nohtyP
"""

#Pedir uma palavra de 6 letras e inverter a leitura da palavra
palavra = input("Digite uma palavra")[::-1]

# Mostra a palavra invertida
print(palavra)

# Resolução alternativa
palavra= "Phyton"
palavra_invertida = palavra[5] + palavra[4] + palavra[3] + palavra[2] + palavra[1] + palavra[0]
print(palavra_invertida)