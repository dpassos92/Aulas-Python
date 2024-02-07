#EX010
"""
Crie um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados.
Ex: 1992
Unidade: 2
Dezena: 9
Centena: 9
Milhar: 1
"""

#Pedir um número de 0 a 9999
num = int(input("Digite um número inteiro entre 0 e 9999"))

#Tratar os dados
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#imprimir no ecrã
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))