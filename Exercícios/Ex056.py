# Ex056
"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando cada dado num dicionário e todos os dicionários numa lista. No final mostre:
a)Quantas pessoas foram registadas;
b)Qual a média de idades do grupo;
c)Quantas mulheres foram registadas;
d)Quantos homens com idade acima da média foram registados.
"""

registos = list()
cont = 0
soma = 0
mulheres = 0
h_acima_media = 0

while True:
    pessoa = {'Nome': input('Digite o nome: ').strip(),
              'Sexo': input('Sexo [M/F]:  ').upper().strip()[0],
              'Idade': int(input('Idade: '))}

    while pessoa['Sexo'] not in 'MF' or pessoa['Idade'] < 0:
        print('Entrada inválida. Por favor, insira um sexo válido (M/F)')
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper().strip()[0]

    while pessoa['Idade'] < 0:
        print('Entrada inválida. Por favor, uma idade não negativa.')
        pessoa['Idade'] = int(input('Idade: '))

    cont += 1
    soma += (pessoa['Idade'])

    if pessoa['Sexo'] in 'Ff':
        mulheres += 1

    registos.append(pessoa)

    print('======' * 5)
    continuar = input('Deseja continuar: [S/N]:').strip().upper()[0]
    if continuar in 'Nn':
        break
    print('======' * 5)

media = soma / cont
for pessoa in registos:
    if pessoa['Sexo'] in 'Mm' and pessoa['Idade'] > media:
        h_acima_media += 1

print(f'Ao todo foram registadas {len(registos)} pessoas.')
print(f'A média de idades das pessoas registadas é: {media:.2f}')
print(f'Ao todo foram registadas {mulheres} mulheres.')
print(f'Ao todo foram registados {h_acima_media} homens acima da média de idades.')


