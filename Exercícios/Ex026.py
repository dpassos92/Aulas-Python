# EX26
"""Faça um programa que leia o ano de nascimento de 7 pessoas e mostre quantas são maiores de idade e quantas não são
maiores de idade.
"""

#imports
from datetime import date
data_actual = date.today().year

#iniciar variáveis de controlo
maiores_idade = 0
menores_idade = 0

#Rodar for para leitura e análise de idades
for c in range(1, 8):
    data_nascimento = int(input(f"Em que ano a {c}º pessoa nasceu\n"))
    if (data_actual - data_nascimento) >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

# Exibir no ecrã os dados
print(f"Temos {maiores_idade} pessoas maiores de idade e {menores_idade} pessoas menores de idade")

