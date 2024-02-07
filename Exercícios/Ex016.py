# EX016
"""
Crie um programa que leia 5 notas de um aluno e calcule a sua média.
>=9.5 passou
>8 e < 9.5 em recuperação
<8 reprova
"""

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
