# EX027
"""
Faça um programa que leia a idade de 10 pessoas. No final mostre qual foi a maior idade lida e a menor.
"""

#iniciar variáveis de controlo
maior = 0
menor = 0

#Rodar for para leitura e análise de idades onde vai guardar os inputs
for pessoa in range(1, 10):
    idade = (input(f"{pessoa}º pessoa - Digite a sua idade: \n"))
    if pessoa == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade


#Exibir a maior e a menor idade
print(f"A maior idade encontrada foi: {maior} anos de idade")
print(f"A menor idade encontrada foi: {menor} anos de idade")