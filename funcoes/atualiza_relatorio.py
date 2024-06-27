from funcoes.adiciona_carrinho import *
from funcoes.importa_relatorio import *
from funcoes.importa_arquivo import *

def atualiza_relatorio():
     
     with open(r'banco_de_dados\relatorio\relatorio.csv', 'a+',encoding='utf-8') as arquivo:
        arquivo.write('codigo' + ';' + 'nome' + ';' + 'marca' + ';' + 'categoria' + ';' + 'total_venda' + ';' + 'valor_total' + '\n')
        for dados in relatorio:
            for dado in carrinho:
                codigo, nome, marca, categoria, quantidade, total = dados  
                codigo_2, nome_2, marca_2, categoria_2, quantidade_2, total_2 = dado
                total_quant = 0
                total_venda = 0       
                if codigo == codigo_2:
                        total_quant = int(quantidade) + int(quantidade)
                        total_venda = float(total) + float(quantidade_2*total_2)
                        arquivo.write(str(codigo) + ';'+ nome + ';' + marca + ';' + categoria + ';' + str(total_quant) + ';' + str(total_venda) + '\n')
            else:
                total_venda = float(quantidade)*float(total)
                arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + str(quantidade) + ';' + str(total_venda) + '\n')