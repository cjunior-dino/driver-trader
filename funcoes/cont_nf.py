import os

def contar_arquivos(diretorio):
    lista_arquivos = os.listdir(diretorio)

    contador = 0

    for item in lista_arquivos:
        if os.path.isfile(os.path.join(diretorio, item)):
            contador += 1

    return contador

diretorio = '/banco_de_dados/historico'
