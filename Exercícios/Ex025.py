# EX025
"""
Faça um programa que leia uma frase qualquer e diga se é um palíndromo, desconsiderando os espaços.
Ex: Anotaram a data da maratona
"""

# Pedir uma frase para saber se é um palíndromo
frase = input("Digita uma frase para saber se é um palíndromo").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]

if juntas == inverso:
    print("A palavra é um palindromo\n")
else:
    print("A palavra não é um palindromo\n")

print(juntas)
print(inverso)

'''# alternativa
frase = input("Digita uma frase para saber se é um palíndromo").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]

tam = len(juntas)

for c in range(0, tam):
    if juntas[c] != inverso[c]:
        print("Não é um palindromo")
        break
    if c == tam -1:
        print("É um palindromo")'''
