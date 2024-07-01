from funcoes.cont_nf import *
nota = []
def buscar_nota(): 

    busca_nf = input("Qual NF deseja buscar?\n-")
    if int(busca_nf) <= contar_arquivos(diretorio):
        with open(rf'banco_de_dados\historico\{busca_nf}.csv', 'r',encoding='utf-8') as arquivo:
            lista_nota = arquivo.readlines()
            for i in lista_nota:
                nota = i.strip('\n').split(';')
                for f in nota:
                    print('\t',f, end='')
                print('\n')
        return True
    else:
        print(" ")
        print("NOTA INEXISTENTE")
        print(" ")
        return True