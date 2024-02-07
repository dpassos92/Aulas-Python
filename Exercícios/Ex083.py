# Ex083
"""
Modifique o exercício 77 para ter atributos privados para titular, saldo e limite.
Implemente getterse setters usando property para esses atributos.
Adicione métodos para depositar() e sacar(), que devem alterar o saldo da conta.
Garanta que as operações respeitem o limite da conta e que o saldo não se torne negativo.
"""

from colorama import init, Fore
from time import sleep

# Initialize colorama
init(autoreset=True)


def main():
    while True:
        print(Fore.GREEN + ":::..Multibanco..:::")
        print(f'[1] Consultar Conta\n'
              f'[2] Depositos\n'
              f'[3] Levantamentos\n'
              f'[4] Sair\n')

        # input for menu choice
        opcao = input("Escolha um opção (1-4): ").strip()
        print()

        if opcao == "1":
            # Calls consultar saldo
            try:
                conta.consultar()

            # Possivel input exceptions from user
            except ValueError:
                print(Fore.RED + 'O utilizador não digitou o número.')

            except KeyboardInterrupt:
                print(Fore.RED + 'O programa foi fechado inesperadamente.')

            finally:
                print(Fore.RED + 'TERMINOU')
                print()

        elif opcao == "2":
            # Calls function depositar
            try:
                valor = int(input('Quantidade a depositar? '))
                conta.depositar(valor)
                print(f'Saldo Atual: {conta.saldo}')
            # Possivel input exceptions from user
            except ValueError:
                print(Fore.RED + 'O utilizador não digitou o número.')

            except KeyboardInterrupt:
                print(Fore.RED + 'O programa foi fechado inesperadamente.')

            finally:
                print(Fore.RED + 'TERMINOU')
                print()

        elif opcao == "3":
            # Calls function levantamento
            try:
                levantar = int(input('Quantidade a levantar? '))
                conta.sacar(levantar)
                print(f'Saldo Atual: {conta.saldo}')
            # Possivel input exceptions from user
            except ValueError:
                print(Fore.RED + 'O utilizador não digitou o número.')

            except KeyboardInterrupt:
                print(Fore.RED + 'O programa foi fechado inesperadamente.')

            finally:
                print(Fore.RED + 'TERMINOU')
                print()

        elif opcao == "4":
            print("Programa a terminar", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".")
            break

        else:
            print(Fore.RED + 'Opção Inválida!! Tente novamente...')
            print()


class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__limite:
            print(f'Não pode levantar mais do que o limite diário de {self.__limite}€')
        elif self.__saldo > valor:
            self.__saldo -= valor

    def consultar(self):
        print(f'Seja bem-vindo {self.__titular}, você tem {self.__saldo}€ na conta.')

    def boas_vindas(self):
        print(Fore.CYAN + f'Bem-vindo {self.__titular}, você tem {self.__saldo}€ na sua conta.'
                          f'\nO seu limite diário de levantamentos é {self.__limite}€')
        print()


conta = ContaBancaria("Diogo", 10000, 1000)
conta.boas_vindas()

main()
