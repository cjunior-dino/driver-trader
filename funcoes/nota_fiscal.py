from funcoes.adiciona_carrinho import carrinho
from funcoes.buscar_nf import *
def nota():
    with open(r'banco_de_dados\historico\dados_nf.csv', 'a+',encoding='utf-8') as arquivo:
        dados = []
        total = 0
        id = 0
        cabecalho = 'NOTA FISCAL' +';' + '-' + ';' + 'N°'+ ';' + str(id) + '\n' + 'COD  ' + ';' + 'PRODUTO' + ';' + 'QUANTIDADE' + ';' +'  VALOR\n'
        arquivo.write(cabecalho)
        for item in range(0, len(carrinho)):
            dados.append((carrinho[item][0], carrinho[item][1], carrinho[item][4],
                        carrinho[item][5]))
            total = total + int(dados[item][2]) * float(dados[item][3])
            guardar = str(dados[item][0] + ';' + dados[item][1] + ';' + str(dados[item][2]) + ';' + str(dados[item][3]) +'\n' )
            arquivo.write(guardar)
        txt = 'Valor Total: ' + ';' + str(round(total,2)) + '\n'
        arquivo.write(txt)