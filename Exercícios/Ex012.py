# EX012
"""
Crie um programa que leia o primeiro e último nome de uma pessoa e exiba as mensagens:
1.“Olá nome, o seu registo está completo.”
2.“O seu email é nome@empresa.pt”
Ex email:
Alfredo Xavier
a.xavier.edu@empresa.pt
"""

# pedir nome
nome = input("Digite o seu primeiro e ultimo nome\n").title()
nome_ultimo = nome.split()

#Apresentar no ecrã o nome
print("Olá {}, o seu registo está completo".format(nome))
#Apresentar o email composto pela primeira letra do primeiro nome e seguido de ponto e ultimo nome, tudo em minusculas
print("O seu email é {}.{}.edu@empresa.pt".format(nome[0].lower(), nome_ultimo[1].lower()))