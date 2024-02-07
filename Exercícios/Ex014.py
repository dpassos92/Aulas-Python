# EX014
"""
Crie um programa que leia um número inteiro introduzido pelo utilizador e que simule um radar de velocidade.
>80km/h multado
<=80km/h não multado
A multa são 100€ + 7€ por cada km/h acima
"""

#Digitar a velocidade do veiculo
velocidade = int(input("Digite a sua velocidade\n"))
#A multa vai ser 100€ + 7€ por cada km/h acima
multa = (velocidade - 80) * 7 + 100

#Declarar as condições
if (velocidade >80):
    print("Você vai ter que pagar {} de multa!".format(multa))
else:
    print("Boa viagem!!")