# Ex070
"""
Crie um sistema que utilize o interactivehelpdo python. O utilizador deve digitar o comando e o sistema deve
retornar o manual. Quando o utilizador digitar “FIM” o programa deve encerrar.
"""


def ajuda_interactiva(funcao):
    help(funcao)
    encerrar =' '
    while encerrar not in 'FIM':
        encerrar = input('Para encerrar o programa digite FIM...').strip().upper()
    return


ajuda = input('Digite o método ou função para ver a sua documentação: ')
print(ajuda_interactiva(ajuda))

