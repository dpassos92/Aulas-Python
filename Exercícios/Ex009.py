#EX009
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantidade de letras sem espaços;
Quantas letras tem o primeiro nome.
"""

#programa para ler nome completo
#Pedir nome
nome_completo = input("Digite o seu nome completo:").strip()
print("Estou a analisar o seu nome!")

# Mostrar o nome em maiusculas
print("O seu nome em maiusculas é{}".format(nome_completo.upper))
print("O seu nome em minusculas é{}".format(nome_completo.lower))

# Mostrar tamanho do nome sem espaços
print("O seu nome tem {} caracteres".format(len(nome_completo) - nome_completo.count(" ")))

# Mostrar tamanho do primeiro nome
p_nome = nome_completo.split()
print("O seu primeiro nome é {} e tem caracteres".format(p_nome[0], len(p_nome[0])))