from funcoes.adiciona_carrinho import carrinho
from funcoes.cont_nf import *

diretorio = 'C:/Users/etech_3050_13_/driver-trader/banco_de_dados/historico'
def nota():
    id = contar_arquivos(diretorio)
    with open(rf'banco_de_dados\historico\{str(id+1)}.csv', 'a+',encoding='utf-8') as arquivo:
        dados = []
        total = 0
        cabecalho = 'NOTA FISCAL ' + ';' + 'N°'+ ';' + str(id+1) + '\n' + 'COD  ' + ';' + 'PRODUTO' + ';' + 'QUANTIDADE' + ';' +'  VALOR\n'
        arquivo.write(cabecalho)
        for item in range(0, len(carrinho)):
            dados.append((carrinho[item][0], carrinho[item][1], carrinho[item][4],
                        carrinho[item][5]))
            total = total + int(dados[item][2]) * float(dados[item][3])
            guardar = str(dados[item][0] + ';' + dados[item][1] + ';' + str(dados[item][2]) + ';' + str(dados[item][3]) +'\n' )
            arquivo.write(guardar)
        txt = 'Valor Total: ' + ';' + str(round(total,2)) + '\n'
        arquivo.write(txt)