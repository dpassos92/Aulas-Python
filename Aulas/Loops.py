'''num = 7

for c in range (0,10):
    print(num, " x ", c + 1, "=", num * (c + 1))
    '''


'''i = 1
f = 10
salto = 2

for michaelJackson in range(i,f,salto):
    print(michaelJackson)'''


# Exemplo
tentativas = 0
mensagem = "Bem Vindo"
password = "Dr.House"

for c in range(0, 3):
    entrada = input("Insira a password: ")
    if entrada == password:
        print(mensagem)
    else:
        tentativas = tentativas + 1
        print("Tente novamente...\n")

    if tentativas == 3:
        print("Utilizador Bloqueado")

# loops
'''contador = 1

while contador <= 10:
    print(contador)
    contador += 1
    '''
'''opcao = 0

while opcao != 4:
    print("[1] - Entrar")
    print("[2] - Definições")
    print("[3] - Like")
    print("[4] - Sair")
    print("Qual a sua opção?")
    opcao = int(input("--->"))
    if opcao < 1 or opcao > 4:
        print("OPÇÃO INVALIDA! TENTE NOVAMENTE!\n")'''


opcao = 0

while opcao != 4:
    print("[1] - Registar pessoa")
    print("[2] - Nº pessoas registadas")
    print("[3] - Apagar um registo")
    print("[4] - Sair")
    print("Qual a sua opção?")
    opcao = int(input("--->"))
    if opcao == 1:
        nome = input("Digite o nome da pessoa")
        idade = int(input("Digite a idade da pessoa"))
        print(f"{nome} Registado com sucesso.\n")
    elif opcao == 2:
        print("Há x pessoas registadas")
    elif opcao == 3:
        print("Um registo foi apagado")
    elif opcao < 1 or opcao > 4:
        print("Seu burro!!")
        break

print("Obrigado volte sempre")