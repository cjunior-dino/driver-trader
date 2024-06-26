relatorio = []

"""Greração do relatorio de vendas"""
def relatorio_prod():
    relatorio.clear()
    with open(r'banco_de_dados\relatorio\relatorio.csv', 'r',encoding='utf-8') as arquivo:
        next(arquivo)
        lista_produtos2 = arquivo.readlines()
        #criando a lista de produto
        for i in lista_produtos2:
            relatorio.append(i.strip('\n').split(';'))

    return relatorio