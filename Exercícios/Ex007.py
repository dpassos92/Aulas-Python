# EX007
"""
Cria um programa que peça o ano de nascimento do utilizador e o ano atual e que calcule a idade do utilizador.
"""

# Pedir ano de nascimento e ano actual
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_actual = int(input("Digite o ano actual: "))

# calcular a idade
idade = ano_actual - ano_nascimento

# Exibir o resultado do calculo da idade
print("\nVocê tem ", idade, "anos")
