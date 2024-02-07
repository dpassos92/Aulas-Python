# Ex069
"""
Desenvolva um programa que permita ao utilizador calcular o seu Índice de Massa Corporal (IMC). O programa deve solicitar ao utilizador a sua altura e o seu peso. De seguida, utilizando uma função, deve calcular o IMC e o programa deve exibir uma mensagem com base no valor do IMC calculado.
●IMC abaixo de 18,5: Abaixo do peso
●IMC entre 18,5 e 24,9: Peso normal
●IMC entre 25,0 e 29,9: Sobrepeso
●IMC entre 30,0 e 34,9: Obesidade grau 1
●IMC entre 35,0 e 39,9: Obesidade grau 2
●IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)
"""

# importar a biblioteca tempo
import time


def apresentacao():
    # Apresentar o programa
    print("-=-" * 10)
    print(f"{'Indice de Massa Corporal':^30}")
    print("-=-" * 10)


def IMC(peso, altura):
    if altura > 3:
        altura = altura / 100

    # Calculo do IMC
    imc = peso / (altura * altura)

    # Inventar texto de apresentação
    print()
    print("A calcular o seu IMC!!\n")
    time.sleep(1.5)
    print("*Musica de elevador*")
    time.sleep(1.5)
    print("Isto está dificil!! Só mais uns segundos.", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".\n")
    time.sleep(1)

    # Apresentar os calculos
    if imc < 18.5:
        return f"O seu IMC é {imc:.2f} e está abaixo do peso"
    elif imc < 24.9:
        return f"O seu IMC é {imc:.2f} e está com peso normal"
    elif imc < 29.9:
        return f"O seu IMC é {imc:.2f} e está com sobrepeso!"
    elif imc < 34.9:
        return f"O seu IMC é {imc:.2f} e está com Obesidade Grau 1"
    elif imc < 39.9:
        return f"O seu IMC é {imc:.2f} e está com Obesidade Grau 2"
    else:
        return f"O seu IMC é {imc:.2f} e está com Obesidade Grau 3 (Obesidade mórbida)"


apresentacao()
p = float(input("\n===Digite o seu peso (Exemplo: 75.0)===\n"))
a = float(input("\n===Digite a sua altura (Exemplo: 1.73)===\n"))

print(IMC(p, a))
