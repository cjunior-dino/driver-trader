produto = []

def adicina():
    produto.clear()
    with open(r'banco_de_dados\produtos\dados.csv', 'r',encoding='utf-8') as arquivo:
        next(arquivo)
        lista_produtos = arquivo.readlines()
        #criado a lista de produto
        for i in lista_produtos:
            produto.append(i.strip('\n').split(';'))
    return produto
