# EX019
"""Crie o jogo da adivinha v1.0. O computador deve “pensar” num número de 0 a 7 e o utilizador deve adivinhar o
número escolhido. O programa deve apresentar se o utilizador venceu ou perdeu.
"""

# Vai buscar a biblioteca tempo e a biblioteca
import time
# Importou tudo da biblioteca random mas podia pedir apenas randint
from random import *

# Pedir um número
print("Jogo da adivinha:\n")
num = int(input("Digita um número de 0 a 7\n"))
# vai parar durante algum tempo até continuar
print("Beep boop!!! Calma estou a pensar!!")
time.sleep(2)
# gerar um número aleatório de 0 a 7
num_aleatorio = randint(0, 7)

# Resposta a comparar o número digitado e o número gerado aleatóriamente
if num == num_aleatorio:
    print(f"Boa pensamos os dois o número {num_aleatorio}!!")
else:
    print(f"Temos pena eu pensei no número {num_aleatorio} e tu no número {num}!!")
