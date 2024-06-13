from funcoes.importa_arquivo import *
from funcoes.adiciona_carrinho import *

def atualiza():
    with open(r'banco_de_dados\produtos\dados.csv', 'w',encoding='utf-8') as arquivo:
        arquivo.write('codigo' + ';' + 'nome' + ';' + 'marca' + ';' + 'categoria' + ';' + 'quantidade' + ';' + 'preco' + '\n')
        for i in produto:
            for j in carrinho:
                codigo, nome, marca, categoria, quantidade, preco = i
                codigo2, nome2, marca2, categoria2, quantidade2, preco2 = j
                if codigo2 == codigo and quantidade != quantidade2:
                    total = int(quantidade) - int(quantidade2)
                    arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + str(total) + ';' + preco + '\n')
                    break
            else:
                arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + quantidade + ';' + preco + '\n')

def atualiza_relatorio():
    with open(r'banco_de_dados\relatorio\relatorio.csv', 'w',encoding='utf-8') as arquivo:
        arquivo.write('codigo' + ';' + 'nome' + ';' + 'marca' + ';' + 'categoria' + ';' + 'quantidade' + ';' + 'preco' + ';'+ 'total' +'\n')
        for i in relatorio:
            for j in carrinho:
                codigo, nome, marca, categoria, quantidade, preco = i
                codigo2, nome2, marca2, categoria2, quantidade2, preco2 = j
                if codigo2 == codigo and quantidade != quantidade2:
                    total = int(quantidade) - int(quantidade2)
                    arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + str(total) + ';' + preco + '\n')
                    break
            else:
                arquivo.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + quantidade + ';' + preco + '\n')
        