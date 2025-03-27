import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor =  conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS materiais")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    peso REAL NOT NULL,
    preco REAL NOT NULL,
    responsavel TEXT NOT NULL,
    data_saida TEXT NOT NULL,
    data_retorno TEXT
)
""")
conexao.commit()

def menu():
        while True:
            print("=========== BEM VINDO AO CONTROLE DE ESTOQUE PARA MATERIAIS PROCESSADOS ===========")
            print("Escolha uma opçao")
            print("[1] Cadastrar Material")
            print("[2] Listar Cadastros")
            print("[3] Pesquisar por Responsavel ou Data")
            print("[4] Sair")

            opcao = input("Escolha uma opçao: ")

            if opcao == '1':
                cadastrar_materiais()
            elif opcao == '2':
                listar_materiais()
            elif opcao == '3':
                pesquisar_materiais()
            elif opcao == '4':
                print("O sistema sera encerrado. Ate a proxima!\n")
                break

            else:
                print("Opcao invalida.")

def cadastrar_materiais():
    nome = input("Informe o material: ")
    tipo = input("Informe o tipo de material? (Bruto ou processado): ")

    try:
        peso = float(input("Informe o peso do material (kg): "))
        preco = float(input("Informe o preço do material (Em kg ou por unidade): "))
    except:
        print("Preço e Peso devem ser valores numericos.")
        return
    
    responsavel = input("Informe o responsavel pelo material: ")
    data_saida = input("Informe a data de saida do material (DD-MM-AAAA): ")

    cursor.execute("INSERT INTO materiais (nome, tipo, peso, preco, responsavel, data_saida, data_retorno) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, tipo, peso, preco, responsavel, data_saida, None))

    conexao.commit()
    print("Atividade cadastrada com sucesso!")

def listar_materiais():
    cursor.execute("SELECT * FROM materiais")
    materiais = cursor.fetchall()

    if not materiais:
        print("Nenhum material cadastrado. \n")
        return
    
    for material in materiais:
        print(f"ID: {material[0]} | Nome: {material[1]} | Tipo: {material[2]} | Peso: {material[3]} | Preço: {material[4]} \n")
        print(f"Responsavel: {material[5]} | Data de Saida: {material[6]} | Data de Retorno: {material[7]}")
        print("-" * 80)

def pesquisar_materiais():
    print("[1] Pesquisar por responsavel")
    print("[2] Pesquisar por data")
    escolha = input("Escolha uma opçao (Digite o numero da opçao)")

    if escolha == '1':
        responsavel = input("Informe o nome do responsavel: ")
        cursor.execute("SELECT * FROM materiais WHERE responsavel = ?", (responsavel,))
    elif escolha == '2':
        data = input("Informe a data (DD-MM-AAAA): ")
        cursor.execute("SELECT * FROM materiais WHERE data_saida = ?", (data,))
    else:
        print("Voce nao digitou uma opçao valida (Apenas [1] e [2]).\n")

    materiais = cursor.fetchall()

    if not materiais:
        print("Nenhum material cadastrado. \n")
        return
    
    for material in materiais:
        print(f"ID: {material[0]} | Nome: {material[1]} | Tipo: {material[2]} | Peso: {material[3]} | Preço: {material[4]} \n")
        print(f"Responsavel: {material[5]} | Data de Saida: {material[6]} | Data de Retorno: {material[7]}")
        print("-" * 80)

menu()

conexao.close()

