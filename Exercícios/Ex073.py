# Ex073
"""
Crie um código em Pythonque teste se o site do IEFP está acessível a partir do seu computador.
"""

import requests


def validar_ligacao(url):
    """
    Validates connection to a given URL.

    :param url: The URL to validate.
    :return: A message indicating the status of the connection.
    """
    try:
        r = requests.get(url)
        print(url)
        if r.status_code == 200:
            return f'Ligação estabelecida!!'
    except requests.exceptions.ConnectionError:
        return f'Não foi possível aceder ao site...Verifique o seu acesso à internet!!'


site = "https://www.iefp.pt"
print(validar_ligacao(site))

