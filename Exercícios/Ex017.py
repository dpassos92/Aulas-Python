# EX017
"""
Crie um programa que leia um número inteiro e peça ao utilizador para escolher a base da conversão:
1 –Binário
2 –Octal
3 –Hexadecimal
"""

#Ler um número inteiro
num = int(input("Digite um número inteiro\n"))
#Ler a opção de escolha
num_convertido = int(input("Escolhe a conversão: \n [1] - Binário; \n [2] - Octal; \n [3] - Hexadecimal\n"))

# Converter o número
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)


#mostrar o num digitado convertido e devolve a partir do index 2
if num_convertido == 1:
    print(f"beep boop  o número {num} em binário é {binario[2:]}")
elif num_convertido == 2:
    print(f"beep boop beep o número {num} em octal é {octal[2:]}")
elif num_convertido == 3:
    print(f"boop beep o número {num} em hexadecimal é {hexadecimal[2:]}")
else:
    print("Estás a gozar?! Só tens 3 opções")