# EX029
"""
Crie o jogo da adivinha v2.0. O computador deve “pensar” num número de 0 a 10 e o utilizador deve adivinhar o
número escolhido. Só que agora o jogador vai tentar adivinhar até acertar. No final mostre quantas tentativas foram
necessárias.
"""

import random

tentativas = 0
pc = random.randint(1, 10)

print("----Jogo da Adivinha----")

while True:
    jogador = int(input("Digita um número de 1 a 10\n"))
    tentativas += 1
    if jogador == pc:
        print(f"Acertaste, pensamos os dois no número {pc}")
        break
    elif jogador < pc:
        print("Errado, mais acima!!\n")
    elif jogador > pc:
        print("Errado, mais abaixo!!\n")


print(f"Foram precisas {tentativas} tentativas")
