#Ex072
"""
Desenvolva um programa que simule uma calculadora interativa com diferentes funcionalidades. O programa deve
exibir um menu com várias opções e permitir que o utilizador escolha uma das opções. O programa deve executar a
funcionalidade escolhida e quando terminar deve voltar a apresentar o menu. Use o tratamento de exceções para lidar
com entradas inválidas (como stringsou caracteres) e erros matemáticos (como divisão por zero). Todas as funções
devem estar num módulo bem estruturado e documentado.

Função-Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]
Função-Tabuada
Função-Par ou Ímpar
Função-Números primos
Função-Factorial
"""

# import libraries
import Funções
from header import header
from time import sleep
from colorama import init, Fore


# Initialize colorama
init(autoreset=True)

while True:
    # calls function header
    header('Funções e Operações Matemáticas')

    # input for menu choice
    opcao = input("Escolha um opção (1-6): ").strip()
    print()

    if opcao == "1":
        # calls function calculadora
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            sinal = input('Que operação deseja fazer? [+ - x /] ').lower().strip()
            print(f'{num1} {sinal} {num2} = {Funções.calculadora(num1, num2, sinal)}')
            print()

        # Possible input exceptions from user
        except ZeroDivisionError:
            print(Fore.RED + 'ERRO!! A DIVISÃO POR ZERO NÃO É POSSÍVEL.')

        except ValueError:
            print(Fore.RED + 'O utilizador não digitou o número.')

        except KeyboardInterrupt:
            print(Fore.RED + 'O programa foi fechado inesperadamente.')

        finally:
            print(Fore.RED + 'TERMINOU')
            print()

    elif opcao == "2":
        # Calls function tabuada
        try:
            tabuada_num = int(input('Digite um número para ver a sua tabuada: '))
            Funções.tabuada(tabuada_num)
            print()
        # Possible input exceptions from user
        except ValueError:
            print(Fore.RED + 'O utilizador não digitou o número.')

        except KeyboardInterrupt:
            print(Fore.RED + 'O programa foi fechado inesperadamente.')

        finally:
            print(Fore.RED + 'TERMINOU')
            print()

    elif opcao == "3":
        # Calls function par_impar
        try:
            par_ou_impar_num = int(input('Digite um número inteiro para saber se é Par ou Ímpar: '))
            Funções.par_impar(par_ou_impar_num)
            print()
        # Possible input exceptions from user
        except ValueError:
            print(Fore.RED + 'O utilizador não digitou o número.')

        except KeyboardInterrupt:
            print(Fore.RED + 'O programa foi fechado inesperadamente.')

        finally:
            print(Fore.RED + 'TERMINOU')
            print()

    elif opcao == "4":
        # Calls function num_primos
        try:
            primo = int(input('Digite um número inteiro para saber se é primo: '))
            Funções.num_primos(primo)
            print()
        # Possible input exceptions from user
        except ValueError:
            print(Fore.RED + 'O utilizador não digitou o número.')

        except KeyboardInterrupt:
            print(Fore.RED + 'O programa foi fechado inesperadamente.')

        finally:
            print(Fore.RED + 'TERMINOU')
            print()

    elif opcao == "5":
        # Calls function factorial
        try:
            num_factorial = int(input('Digite um número calcular o factorial: '))
            opcao = input('Deseja ver o processo? [S/N]\n--->').strip().lower()
            mostra = True if opcao == 's' else False
            resultado = Funções.factorial(num_factorial, mostra)
            print(resultado)
            print()
        # Possible input exceptions from user
        except ValueError:
            print(Fore.RED + 'O utilizador não digitou o número.')

        except KeyboardInterrupt:
            print(Fore.RED + 'O programa foi fechado inesperadamente.')

        finally:
            print(Fore.RED + 'TERMINOU')
            print()

    elif opcao == "6":
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
