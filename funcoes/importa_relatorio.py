relatorio2 = []

"""Greração do relatorio de vendas"""
def relatorio_prod():
    relatorio2.clear()
    with open(r'banco_de_dados\relatorio\relatorio.csv', 'r',encoding='utf-8') as arquivo:
        next(arquivo)
        lista_produtos = arquivo.readlines()
        #criando a lista de produto
        for i in lista_produtos:
            relatorio2.append(i.strip('\n').split(';'))
    print(relatorio2)
    return relatorio2