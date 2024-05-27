import csv

# Função para ler os dados de login e senha do arquivo CSV
def ler_dados_login(arquivo_csv):
    dados_login = {}
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Pular o cabeçalho
        for row in reader:
            login, senha = row
            dados_login[login] = senha
    return dados_login

# Função para verificar o login
def verificar_login(dados_login, login, senha):
    if login in dados_login and dados_login[login] == senha:
        return True
    return False

# Programa principal
def main():
    arquivo_csv = 'dados_login.csv'
    dados_login = ler_dados_login(arquivo_csv)
    
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    if verificar_login(dados_login, login, senha):
        print("Login bem-sucedido!")
    else:
        print("Login ou senha incorretos.")

if _name_ == "_main_":
    main()
