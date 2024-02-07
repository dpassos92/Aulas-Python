# Ex035
"""
Tabuada V2.0 –Faça um programa que mostre a tabuada de vários números inseridos pelo utilizador. O programa deverá
ser interrompido quando o número inserido for negativo ou 0.
"""

print('========Tabuada v2.0========')
while True:
    num = int(input('Digite um número: '))
    print('==='*7)
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('==='*7)
    print('Para parar digite [0] ou um número negativo...')
print('=====================')