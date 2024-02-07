# Ex085
"""
Crie o jogo Pedra, Papel, Tesoura com orientação para objetos.
"""

from random import randint
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


def main():
    while True:
        print(Fore.GREEN + f'----Pedra, Papel, Tesoura----')
        print('[1] - Pedra\n'
              '[2] - Papel\n'
              '[3] - Tesoura')
        try:
            valor_jogador = int(input('Escolha a sua opção ----> '))
            if not 1 <= valor_jogador <= 3:
                raise ValueError(Fore.RED + f'Jogada inválida...Tente novamente...')
        except ValueError:
            print(Fore.RED + f'Jogada inválida...Tente novamente...')
            print()
            continue

        valor_pc = randint(1, 3)
        jogar = Jogo(valor_pc, valor_jogador)

        print()
        print(jogar.ler_escolha_jogador(), end=' e o ')
        print(jogar.ler_escolha_pc())
        print(jogar.resultado())
        print()

        continuar = input('Quer continuar? [S/N]').strip().upper()
        while True:
            if continuar == 'N':
                print('A terminar... Até à proxima!!')
                break
            if continuar != 'S':
                print('Opção Inválida... tente novamente')
                continuar = input('Quer continuar? [S/N]').strip().upper()
            else:
                break
        print()
        if continuar == 'N':
            break


class Jogo:
    def __init__(self, valor_pc, valor_jogador):
        self.__valor_pc = valor_pc
        self.__valor_jogador = valor_jogador

    @property
    def pc(self):
        return self.__valor_pc

    @pc.setter
    def pc(self, valor_pc):
        self.__valor_pc = valor_pc

    @property
    def jogador(self):
        return self.__valor_jogador

    @jogador.setter
    def jogador(self, valor_jogador):
        self.__valor_jogador = valor_jogador

    def jogada_pc(self):
        valor = randint(1, 3)
        self.__valor_pc = valor

    def jogada_do_jogador(self, valor):
        self.__valor_jogador = valor

    def ler_escolha_jogador(self):
        valor_j = self.__valor_jogador

        if valor_j == 1:
            return f'O Jogador escolheu Pedra'
        elif valor_j == 2:
            return f'O Jogador escolheu Papel'
        elif valor_j == 3:
            return f'O Jogador escolheu Tesoura'

    def ler_escolha_pc(self):
        valor_p = self.__valor_pc
        if valor_p == 1:
            return f'PC escolheu Pedra'
        elif valor_p == 2:
            return f'PC escolheu Papel'
        elif valor_p == 3:
            return f'PC escolheu Tesoura'

    def resultado(self):
        calculo_resultado = self.__valor_jogador - self.__valor_pc
        if calculo_resultado == -2 or calculo_resultado == 1:
            return Fore.BLUE + f'Jogador ganhou!'
        elif calculo_resultado == 0:
            return Fore.YELLOW + f'Empatou!!'
        else:
            return Fore.RED + f'Jogador Perdeu!!'


main()
