# criar uma conta bancária
# identidade, títular, saldo, limite
# levantar dinheiro, depositar dinheiro, extrato

'''contas = list()

while True:
    conta = {"identidade": input('ID: '),
             "titular": input('Títular: '),
             "saldo": input('Saldo: '),
             "limite": input('Limite: ')
             }
    contas.append(conta)
    opcao = input('Deseja registar mais? ').strip().lower()
    if opcao == 'n':
        break

print(contas)'''

'''#
def levantar_dinheiro(valor):
    if valor > conta["limite"]:
        print("O seu limite é de 400€")
    else:
        conta["saldo"] -= valor


def depositar_dinheiro(valor):
    conta["saldo"] += valor


def extrato():
    print(f'A conta {conta["identidade"]} tem o saldo de {conta["saldo"]}')


conta = {"identidade": input('ID: '),
         "titular": input('Títular: '),
         "saldo": int(input('Saldo: ')),
         "limite": int(input('Limite: '))
         }

print("Extrato")
extrato()
print("Deposito de 1000")
depositar_dinheiro(1000)
print("Extrato")
extrato()
print("erro de limite")
levantar_dinheiro(1000)
print("Extrato")
extrato()
print("Deposito de 400")
levantar_dinheiro(400)
print("Extrato")
extrato()'''

'''#
class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco


jogo = Jogo("Palworld", "PC", 29.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)'''

'''#
class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.__identidade = identidade
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def levantar(self, valor):
        if valor > self.__limite:
            print("O seu limite é de 400€ diários.")
        else:
            if self.__saldo > valor:
                self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f"A conta {self.__identidade} tem {self.__saldo}€ disponíveis")

'''


'''#
class Conta:
    def __init__(self, nib, titular, saldo, limite):
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite (self, valor):
        self.__limite = valor'''

'''
class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return f'O saldo da conta é {self.__saldo}€'

    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print('Valor não autorizado')
        else:
            self.__saldo = valor
            print('Saldo modificado com sucesso!!')


conta = Conta("Ricardo", 1250, 400)
print(conta.saldo)
conta.saldo = 999
print(conta.saldo)
'''

class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return (f'Titular: {self.titular}\n'
                f'Saldo: {self.saldo}\n')


conta_pessoal = ContaBancaria("Ricardo", 1250, 400)
print(conta_pessoal)