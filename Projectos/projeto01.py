print("-------------------------------------------------")
print("------ Seja bem vindo ao calculador de imc ------")
print("-------------------------------------------------\n")

altura = float(input("Qual a sua altura (1.75): "))
peso = float(input("Qual o seu peso (70.0): "))

imc = round(peso / (altura * altura), 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
elif imc >= 40.0:
    print("Obesidade mórbida")
