#EX011
"""
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “A”;
Em que posição aparece a primeira vez;
Em que posição aparece a última vez.
"""

#Pedir uma frase
frase = input("Digite uma frase").upper().strip()

#analisar a frase
print("A frase tem {} letras A presentes".format(frase.count("A")))
print("A letra A aparece pela primeira vez na posição {}".format(frase.find("A")+1))
print("A letra A aparece pela última vez na posiçãao {}".format(frase.rfind("A")+1))