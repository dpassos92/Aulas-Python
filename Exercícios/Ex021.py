# EX021
"""Faça um programa que simule uma contagem regressiva para a passagem de ano, de 10 até 0, com 1 segundo de pausa
entre eles.
"""

import os
import time
# Constante de tempo
contagem = 10

# Apresenta uma contagem regressiva a partir de um número inicial, neste caso contagem
for c in range(0,10):
    print(contagem - c)
    time.sleep(1)
    if (contagem - c) == 1:
        print("FELIZ ANO NOVO!!!!")
        os.system("leitura.mp3")