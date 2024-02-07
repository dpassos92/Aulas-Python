# Ex079
"""
Crie uma classe ContaBancariacom atributos privados nib, titular, saldo e limite. Adicione métodos getterse
setters para os atributos.
"""


class ContaBancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_nib(self):
        return f'O seu NIB é: {self.__nib}'

    def set_nib(self, nib):
        self.__nib = nib

    def get_titular(self):
        return f'O Títular da conta é: {self.__titular}'

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return f'O saldo da conta é: {self.__saldo}'

    def set_saldo(self, saldo):
        self.__saldo += saldo

    def get_limite(self):
        return f'O limite da conta é: {self.__limite}'

    def set_limite(self, limite):
        self.__limite = limite


nib = int(input('NIB: '))
titular = input('Titular: ')
saldo = float(input('Saldo: '))
limite = float(input('Limite: '))

conta = ContaBancaria(nib, titular, saldo, limite)
print(conta.get_nib())
print(conta.get_titular())
print(conta.get_saldo())
print(conta.get_limite())

while True:
    print()
    opcao = input('Deseja mudar os dados da conta? [S/N] ').strip().upper()
    if opcao == 'S':
        novo_nib = int(input('Novo NIB: '))
        novo_titular = input('Novo Titular: ')
        novo_saldo = float(input('Novo Saldo: '))
        novo_limite = float(input('Novo Limite: '))
        conta = ContaBancaria(novo_nib, novo_titular, novo_saldo, novo_limite)
        print(conta.get_nib())
        print(conta.get_titular())
        print(conta.get_saldo())
        print(conta.get_limite())
    elif opcao == 'N':
        print('Terminou...')
        break
    else:
        print('Opção inválida...')
