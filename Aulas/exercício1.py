'''# EX001 (\n) dá parágrafo dentro do print()
print("Olá Mundo!\n\n")

# EX002
name = input("Digite o seu nome")

print("Olá", name, "\n\n")

# EX003
numero_a = int(input("Digite o primeiro número"))
numero_b = int(input("Digite o segundo número"))
resultado = numero_a + numero_b

print(numero_a, "+", numero_b, "=", resultado, "\n\n")

# EX004
num1 = int(input("Digite um número"))
num_antecessor = num1 - 1
num_sucessor = num1 + 1

print("O número antecessor ao digitado é:", num_antecessor)
print("O número sucessor do digitado é:", num_sucessor)'''
'''import random'''

'''# EX005
# Ler números do utilizador
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Estruturar variáveis e calculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

# Apresentar resultados no ecrã
print("\nSoma =", num1, "+", num2, "=", soma)
print("Subtração =", num1, "-", num2, "=", subtracao)
print("Multiplicação =", num1, "*", num2, "=", multiplicacao)
print("Divisão =", num1, "/", num2, "=", divisao)
print("Resto =", num1, "%", num2, "=", resto)
'''

'''# EX006
# Inserir 5 notas para cálcular a média
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))
nota5 = float(input("Digite a quinta nota:"))

#calcular a média
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#exibir a nota
print("\nA sua média final é:10", media)'''

'''# EX007
# Pedir ano de nascimento e ano actual
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_actual = int(input("Digite o ano actual: "))

# calcular a idade
idade = ano_actual - ano_nascimento

# Exibir o resultado do calculo da idade
print("\nVocê tem ", idade, "anos")'''

''''# EX008
# Pedir o número de Km percorrido e o número de dias que o carro foi alugado
num_km_percorridos = float(input("Digite o número de Km percorridos pelo carro: "))
num_dias_alugado = int(input("Digite o número de dias que o carro foi alugado: "))

# variáveis de calculo
CUSTO_DIA = 60
CUSTO_KM = 0.456

# Calculo do total a pagar sabendo que é 60€ por dia e 0.456€ por Km percorrido
pagar = (CUSTO_DIA * num_dias_alugado) + (CUSTO_KM * num_km_percorridos)

# Exibir o total a pagar
print("\nVocê tem que pagar: ", pagar, "€")'''

'''#EX009
#programa para ler nome completo
#Pedir nome
nome_completo = input("Digite o seu nome completo:").strip()
print("Estou a analisar o seu nome!")

# Mostrar o nome em maiusculas
print("O seu nome em maiusculas é{}".format(nome_completo.upper))
print("O seu nome em minusculas é{}".format(nome_completo.lower))

# Mostrar tamanho do nome sem espaços
print("O seu nome tem {} caracteres".format(len(nome_completo) - nome_completo.count(" ")))

# Mostrar tamanho do primeiro nome
p_nome = nome_completo.split()
print("O seu primeiro nome é {} e tem caracteres".format(p_nome[0], len(p_nome[0])))
'''

'''#EX010
#Pedir um número de 0 a 9999
num = int(input("Digite um número inteiro entre 0 e 9999"))

#Tratar os dados
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#imprimir no ecrã
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
'''

'''#EX011
#Pedir uma frase
frase = input("Digite uma frase").upper().strip()

#analisar a frase
print("A frase tem {} letras A presentes".format(frase.count("A")))
print("A letra A aparece pela primeira vez na posição {}".format(frase.find("A")+1))
print("A letra A aparece pela última vez na posiçãao {}".format(frase.rfind("A")+1))
'''

'''# EX012
# pedir nome
nome = input("Digite o seu primeiro e ultimo nome\n").title()
nome_ultimo = nome.split()

#Apresentar no ecrã o nome
print("Olá {}, o seu registo está completo".format(nome))
#Apresentar o email composto pela primeira letra do primeiro nome e seguido de ponto e ultimo nome, tudo em minusculas
print("O seu email é {}.{}.edu@empresa.pt".format(nome[0].lower(), nome_ultimo[1].lower()))
'''

'''# EX013
#Pedir uma palavra de 6 letras e inverter a leitura da palavra
palavra = input("Digite uma palavra")[::-1]

# Mostra a palavra invertida
print(palavra)

# Resolução alternativa
palavra= "Phyton"
palavra_invertida = palavra[5] + palavra[4] + palavra[3] + palavra[2] + palavra[1] + palavra[0]
print(palavra_invertida)'''

'''# EX014
#Digitar a velocidade do veiculo
velocidade = int(input("Digite a sua velocidade\n"))
#A multa vai ser 100€ + 7€ por cada km/h acima
multa = (velocidade - 80) * 7 + 100

#Declarar as condições
if (velocidade >80):
    print("Você vai ter que pagar {} de multa!".format(multa))
else:
    print("Boa viagem!!")'''

'''# EX015

num = int(input("Digite um número inteiro\n"))

if num % 2 == 0:
    print("O número é par")
else:
    print("O seu número é impar!")
'''

''''# EX016
#Ler as 5 notas de um aluno
nota_1 = float(input("Digite a primeira nota:\n"))
nota_2 = float(input("Digite a segunda nota:\n"))
nota_3 = float(input("Digite a terceira nota:\n"))
nota_4 = float(input("Digite a quarta nota:\n"))
nota_5 = float(input("Digite a quinta nota:\n"))

#calcular a média
media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

#fazer validação15.4
if media >= 9.5:
    print(f"Passou a com {media:.2f}")
elif media >= 8 and media < 9.5:
    print(f"Reprovou mas está em recuperação com média de {media:.2f}")
else:
    print(f"Reprovou com {media:.2f}, tem que estudar mais")
'''

'''# EX017
#Ler um número inteiro
num = int(input("Digite um número inteiro\n"))
#Ler a opção de escolha
num_convertido = int(input("Escolhe a conversão: \n [1] - Binário; \n [2] - Octal; \n [3] - Hexadecimal\n"))

# Converter o número
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)


#mostrar o num digitado convertido e devolve a partir do index 2
if num_convertido == 1:
    print(f"beep boop  o número {num} em binário é {binario[2:]}")
elif num_convertido == 2:
    print(f"beep boop beep o número {num} em octal é {octal[2:]}")
elif num_convertido == 3:
    print(f"boop beep o número {num} em hexadecimal é {hexadecimal[2:]}")
else:
    print("Estás a gozar?! Só tens 3 opções")'''


'''#EX018
import time
#Ler dois números inteiros
num1 = int(input("Digita um número\n"))
num2 = int(input("Digita outro número\n"))
time.sleep(1)

#Compara os números
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num1 < num2:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print(f"Os números são iguais!!")'''

'''# EX019
# Vai buscar a biblioteca tempo e a biblioteca
import time
# Importou tudo da biblioteca random mas podia pedir apenas randint
from random import *

# Pedir um número
print("Jogo da adivinha:\n")
num = int(input("Digita um número de 0 a 7\n"))
# vai parar durante algum tempo até continuar
print("Beep boop!!! Calma estou a pensar!!")
time.sleep(2)
# gerar um número aleatório de 0 a 7
num_aleatorio = randint(0, 7)

# Resposta a comparar o número digitado e o número gerado aleatóriamente
if num == num_aleatorio:
    print(f"Boa pensamos os dois o número {num_aleatorio}!!")
else:
    print(f"Temos pena eu pensei no número {num_aleatorio} e tu no número {num}, nabo!!")
'''

'''# EX020
import time

import random

# input do jogador
print("Jogo do Pedra, Papel, Tesoura")

jogador = int(input("Escolhe a tua opção: \n [1] Pedra \n [2] Papel \n [3] Tesoura\n"))
time.sleep(2)

#escolha do pc
pc = random.randint(1,3)

# Resultados do jogo

if jogador == pc:
    print(f"Empate")
elif (jogador - pc) == -2 or (jogador - pc) == 1:
    print(f"Ganhaste!!")
elif (jogador - pc) == -1 or (jogador - pc) == 2:
    print(f"Perdeste!!")'''

'''# EX021
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
        os.system("leitura.mp3")'''

'''# EX022
# Mostra os números pares de 1 a 100
for c in range(1,101,2):
    print(c+1)'''

'''# Alternativa
i = 0
f =100

for c in range(i, f):
    if c == 0:
        continue
    elif c % 2 == 0:
        print(c)'''

'''# EX023
# Pedir um número
num = int(input("Digite um número para ver a sua tabuada: \n"))


print(f"Tabuada do {num}: \n")
for c in range(0, 10):
    print(num, "x", c + 1, "=", num * (c + 1))'''

'''# EX024
#Pedir um número e verificar se é número primo
num = int(input("Digite um número: \n"))

#Para sabermos se um número é primo temos que saber a sua raiz quadrada e dividir por todos os números menores que a sua raiz quadrada
raiz_quadrada = int(num ** 0.5)

# Verificar se o número é maior que 1, pois números menores que 2 não são primos
if num > 1:
    #Loop para verificar se o número é divisível por algum número de 2 até a raiz quadrada do número
    for c in range(2, raiz_quadrada + 1):
        if num % c == 0:
            print("Não é número primo")
            #Se o loop for concluído sem ser interrompido pelo break, o bloco de código dentro do else é executado
            break
    else:
        print("É um número primo")
else:
    print("Não é um número primo")'''


''''#alternativa
#Pedir um número e verificar se é número primo
num = int(input("Digite um número: \n"))
tot = 0

for c in range (1, num +1):
    if num % c == 0:
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[33m", end="")

if tot == 2:
    print(f"O númmero {num} é PRIMO, foi divisível {tot} vezes.")
else:
    print(f"O número {num} não é primo, foi divisivel {tot} vezes.")'''


'''# EX025
# Pedir uma frase para saber se é um palíndromo
frase = input("Digita uma frase para saber se é um palíndromo").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]

if juntas == inverso:
    print("A palavra é um palindromo\n")
else:
    print("A palavra não é um palindromo\n")

print(juntas)
print(inverso)'''

'''# alternativa
frase = input("Digita uma frase para saber se é um palíndromo").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]

tam = len(juntas)

for c in range(0, tam):
    if juntas[c] != inverso[c]:
        print("Não é um palindromo")
        break
    if c == tam -1:
        print("É um palindromo")'''

'''# EX26
#imports
from datetime import date
data_actual = date.today().year

#iniciar variáveis de controlo
maiores_idade = 0
menores_idade = 0

#Rodar for para leitura e análise de idades
for c in range(1, 8):
    data_nascimento = int(input(f"Em que ano a {c}º pessoa nasceu\n"))
    if (data_actual - data_nascimento) >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

# Exibir no ecrã os dados
print(f"Temos {maiores_idade} pessoas maiores de idade e {menores_idade} pessoas menores de idade")'''

'''# EX027
#iniciar variáveis de controlo
maior = 0
menor = 0

#Rodar for para leitura e análise de idades onde vai guardar os inputs
for pessoa in range(1, 10):
    idade = (input(f"{pessoa}º pessoa - Digite a sua idade: \n"))
    if pessoa == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade


#Exibir a maior e a menor idade
print(f"A maior idade encontrada foi: {maior} anos de idade")
print(f"A menor idade encontrada foi: {menor} anos de idade")'''

'''# EX 028
# Desenvolva um programa que faça 3 perguntas e apenas aceite como resposta "V" ou "F". Caso esteja errado pedir para repetir

print("Responde apenas verdadeiro (V) ou falso (F) às seguintes questões: ")

#definir variável
resposta = ""

#Loop para a primeira questão
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
#Loop para a segunda questão
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
#Loop para a terceira pergunta
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
'''

'''#alternativa
# definir variáveis
resp = 0

#primeira pergunta
print("A Lua é maior que o Sol.")
print("V ou F?")
resp = input("--->>>").strip().upper()

#loop para ter a resposta adequada
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
    print("Está certo!!\n\n")'''

'''# EX029
import random

tentativas = 0
pc = random.randint(1, 10)

print("----Jogo da Adivinha----")

while True:
    jogador = int(input("Digita um número de 1 a 10\n"))
    tentativas += 1
    if jogador == pc:
        print(f"Acertaste, pensamos os dois no número {pc}")
        break
    elif jogador < pc:
        print("Errado, mais acima!!\n")
    elif jogador > pc:
        print("Errado, mais abaixo!!\n")


print(f"Foram precisas {tentativas} tentativas")'''

