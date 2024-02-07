# EX008
"""Crie um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias que foi
alugado. Apresente o total a pagar sabendo que o carro custa 60€/dia e 0.456€/km."""

# Pedir o número de Km percorrido e o número de dias que o carro foi alugado
num_km_percorridos = float(input("Digite o número de Km percorridos pelo carro: "))
num_dias_alugado = int(input("Digite o número de dias que o carro foi alugado: "))

# variáveis de calculo
CUSTO_DIA = 60
CUSTO_KM = 0.456

# Calculo do total a pagar sabendo que é 60€ por dia e 0.456€ por Km percorrido
pagar = (CUSTO_DIA * num_dias_alugado) + (CUSTO_KM * num_km_percorridos)

# Exibir o total a pagar
print("\nVocê tem que pagar: ", pagar, "€")