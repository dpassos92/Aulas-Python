# Ex077
"""
Crie uma classe ContaBancariacom atributos titular, saldo e limite. Adicione métodos para depositar() e sacar(),
alterando o saldo da conta de acordo com a operação.
"""

from colorama import init, Fore
from time import sleep

# Initialize colorama
init(autoreset=True)


class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.limite:
            print(f'Não pode levantar mais do que o limite diário de {self.limite}€')
        elif self.saldo > valor:
            self.saldo -= valor

    def consultar(self):
        print(f'Seja bem-vindo {self.titular}, você tem {self.saldo}€ na conta.')

    def boas_vindas(self):
        print(Fore.CYAN + f'Bem-vindo {self.titular}, você tem {self.saldo}€ na sua conta.'
                          f'\nO seu limite diário de levantamentos é {self.limite}€')
        print()


conta = ContaBancaria("Diogo", 10000, 1000)
conta.boas_vindas()

while True:
    print(Fore.GREEN+":::..Multibanco..:::")
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
            deposito = int(input('Quantidade a depositar? '))
            conta.depositar(deposito)
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
