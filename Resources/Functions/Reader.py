import os
import datetime


def getProperty(valor):
    path_config = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Properties/config.txt'))
    arq = open(path_config.replace(os.sep, '/'), 'r')
    texto = arq.readlines()
    for linha in texto:
        valor_prop = linha.split('=')
        if valor_prop[0] == valor:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', valor_prop[1].strip(" ")))
            arq.close()
            return path.replace(os.sep, '/').strip("\n")

    return "Property não encontrada"



