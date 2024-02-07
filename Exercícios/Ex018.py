#EX018
"""
Crie um programa que leia dois números inteiros e compare-os da seguinte forma:
-O primeiro número é maior;
-O segundo número é maior;
-Os números são iguais.
"""

import time
#Ler dois números inteiros
num1 = int(input("Digita um número\n"))
num2 = int(input("Digita outro número\n"))
time.sleep(1)

#Compara os números
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num1 < num2:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print(f"Os números são iguais!!")