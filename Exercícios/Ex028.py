# EX 028
# Desenvolva um programa que faça 3 perguntas e apenas aceite como resposta "V" ou "F". Caso esteja errado pedir para repetir

print("Responde apenas verdadeiro (V) ou falso (F) às seguintes questões: ")

# definir variável
resposta = ""

# Loop para a primeira questão
while resposta != "V" or resposta != "F":
    resposta = input("A Lua é maior que o Sol. V ou F?\n").upper()
    if resposta == "V":
        print("Resposta errada!\n")
        break
    elif resposta == "F":
        print("Resposta certa!\n")
        break
    else:
        print("A sua resposta não está na formatação pedida!!")
# Loop para a segunda questão
while resposta != "V" or resposta != "F":
    resposta = input("O Brasil é o país mais populoso do mundo. V ou F?\n").upper()
    if resposta == "V":
        print("Resposta errada!\n")
        break
    elif resposta == "F":
        print("Resposta certa!\n")
        break
    else:
        print("A sua resposta não está na formatação pedida!!\n")
# Loop para a terceira pergunta
while resposta != "V" or resposta != "F":
    resposta = input("O diamante é a substância mais dura encontrada na natureza. V ou F? \n").upper()
    if resposta == "V":
        print("Resposta certa!\n")
        break
    elif resposta == "F":
        print("Resposta errada\n")
        break
    else:
        print("A sua resposta não está na formatação pedida!!")


'''  # alternativa
# definir variáveis
resp = 0

# primeira pergunta
print("A Lua é maior que o Sol.")
print("V ou F?")
resp = input("--->>>").strip().upper()

# loop para ter a resposta adequada
while resp not in "VF":
    print("Por favor digite V para verdadeiro ou F para falso")
    resp = input("--->>>").strip().upper()

# validação da primeira pergunta
if resp in "F":
    print("Está errado!!!\n\n")
elif resp in "V":
    print("Está certo!!\n\n")

# segunda pergunta
print("O Brasil é o país mais populoso do mundo.")
print("V ou F?")
resp = input("--->>>").strip().upper()

# loop para ter a resposta adequada
while resp not in "VF":
    print("Por favor digite V para verdadeiro ou F para falso")
    resp = input("--->>>").strip().upper()

# validação da segunda pergunta
if resp in "F":
    print("Está errado!!!\n\n")
elif resp in "V":
    print("Está certo!!\n\n")

# primeira terceira pergunta
print("O diamante é a substância mais dura encontrada na natureza.")
print("V ou F?")
resp = input("--->>>").strip().upper()

# loop para ter a resposta adequada
while resp not in "VF":
    print("Por favor digite V para verdadeiro ou F para falso")
    resp = input("--->>>").strip().upper()

# validação da terceira pergunta
if resp in "F":
    print("Está errado!!!\n\n")
elif resp in "V":
    print("Está certo!!\n\n")
    '''