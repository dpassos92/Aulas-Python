from colorama import init, Fore


# Initialize colorama
init(autoreset=True)


def header(msg):
    padding = (60 - len(msg)) // 2
    print('=' * (padding + len(msg) + padding))
    print(Fore.GREEN + f'{msg:^60}')
    print('=' * (padding + len(msg) + padding))

    print(f'[1] Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]\n'
          f'[2]Tabuada\n'
          f'[3] Par ou Ímpar\n'
          f'[4] Números Primos\n'
          f'[5] Factorial\n'
          f'[6] Sair\n')
