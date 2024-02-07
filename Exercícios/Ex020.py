# EX020
"""
Crie o jogo pedra, papel, tesoura.
"""
import time
import random

# input do jogador
print("Jogo do Pedra, Papel, Tesoura")

jogador = int(input("Escolhe a tua opção: \n [1] Pedra \n [2] Papel \n [3] Tesoura\n"))
time.sleep(2)

#escolha do pc
pc = random.randint(1,3)

# Resultados do jogo

if jogador == pc:
    print(f"Empate")
elif (jogador - pc) == -2 or (jogador - pc) == 1:
    print(f"Ganhaste!!")
elif (jogador - pc) == -1 or (jogador - pc) == 2:
    print(f"Perdeste!!")