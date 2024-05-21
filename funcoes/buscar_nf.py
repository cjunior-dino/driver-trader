dados_notas = []
def buscar_nota(): 
    
    with open(r'banco_de_dados\historico\dados_nf.csv', 'r',encoding='utf-8') as arquivo:
        lista_notas = arquivo.readlines()
        for i in lista_notas:
            dados_notas.append(i.strip('\n').split('°'))