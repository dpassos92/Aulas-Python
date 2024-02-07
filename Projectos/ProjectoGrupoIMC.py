#importar a biblioteca tempo
import time

#Apresentar o programa
print("="*25)
print("Indice de Massa Corporal")
print("="*25)

#Pedir os inputs de peso e altura e converter a altura caso alguém insira em cm
peso = float(input("===Digite o seu peso (Exemplo: 75.0)===\n"))
altura = float(input("===Digite a sua altura (Exemplo: 1.73)===\n"))
if altura > 3:
    altura = altura / 100

#Calculo do IMC
imc = peso / (altura*altura)

#Inventar texto de apresentação
print("A calcular o seu IMC!!\n")
time.sleep(2)
print("*Musica de elevador*\n")
time.sleep(2)
print("Isto está dificil!! Só mais uns segundos\n")
time.sleep(2)

#Apresentar os calculos
if imc < 18.5:
    print(f" O seu IMC é {round(imc, 2)} e está abaixo do peso")
elif imc < 24.9:
    print(f"O seu IMC é {round(imc, 2)} e está com peso normal")
elif imc < 29.9:
    print(f"O seu IMC é {round(imc, 2)} e está com sobrepeso!")
elif imc < 34.9:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade Grau 1")
elif imc < 39.9:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade Grau 2")
else:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade Grau 3 (Obesidade mórbida)")
