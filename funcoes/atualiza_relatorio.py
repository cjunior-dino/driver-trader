from funcoes.adiciona_carrinho import *
from funcoes.importa_relatorio import *
lis = []
def atualiza_relatorio():
    lis.clear()
    print("atualiza")
    relatorio_prod()
    a = 0
    with open(r'banco_de_dados\relatorio\relatorio.csv', 'w',encoding='utf-8') as arquivo:
        arquivo.write('codigo' + ';' + 'nome' + ';' + 'marca' + ';' + 'categoria' + ';' + 'total_venda' + ';' + 'valor_total' + '\n')
        for dados in relatorio2:
            for dado in carrinho:
                codigo, nome, marca, categoria, quantidade, total = dados
                codigo2, nome2, marca2, categoria2, quantidade2, total2 = dado
                total_quant = 0
                total_venda = 0       
                if codigo == codigo2:
                        total_quant = int(quantidade) + int(quantidade2)
                        total_venda = float(total) + (float(quantidade2)*float(total2))
                        arquivo.write(str(codigo) + ';'+ nome + ';' + marca + ';' + categoria + ';' + str(total_quant) + ';' + str(total_venda) + '\n')
                        break
            else:
                arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + quantidade + ';' + total + '\n')
                