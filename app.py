import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor =  conexao.cursor()

""" cursor.execute("DROP TABLE IF EXISTS materiais") """ 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    peso REAL NOT NULL,
    preco REAL NOT NULL,
    responsavel TEXT NOT NULL,
    data_saida TEXT NOT NULL,
    data_retorno TEXT,
    rendimento REAL
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
            print("[4] Retorno e Rendimento")
            print("[5] Sair")

            opcao = input("Escolha uma opçao: ")

            if opcao == '1':
                cadastrar_materiais()
            elif opcao == '2':
                listar_materiais()
            elif opcao == '3':
                pesquisar_materiais()
            elif opcao == '4':
                calcular_rendimento()
            elif opcao == '5':
                print("O sistema sera encerrado. Ate a proxima!\n")
                break

            else:
                print("Opcao invalida.")

def cadastrar_materiais():
    nome = input("Informe o material: ")
    tipo = input("Informe o tipo de material? (Bruto ou processado): ")

    try:
        peso = float(input("Informe o peso/quantidade do material (Em kg ou por unidade): "))
        preco = float(input("Informe o preço do material (Em kg ou por unidade): "))
    except:
        print("Preço e Peso devem ser valores numericos.")
        return
    
    responsavel = input("Informe o responsavel pelo material: ")
    data_saida = input("Informe a data de saida do material (DD-MM-AAAA): ")

    cursor.execute("INSERT INTO materiais (nome, tipo, peso, preco, responsavel, data_saida, data_retorno, rendimento) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, tipo, peso, preco, responsavel, data_saida, None , None))

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

def calcular_rendimento():
    listar_materiais()
    id_material = input("Informe o ID do material que retornou: ")
    cursor.execute("SELECT peso FROM materiais WHERE id = ?", (id_material,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("ID não encontrado...\n")
        return

    peso_inicial = resultado[0]
    peso_retorno = float(input("Informe o peso do material já processado: "))
    data_retorno = input("Informe a data de retorno do material processado: ")

    rendimento = (peso_retorno / peso_inicial) * 100
    perda = 100 - rendimento

    cursor.execute(""" UPDATE materiais
                   SET peso_retorno = ?, data_retorno = ?, rendimento = ?
                   WHERE id = ?""", (peso_retorno,data_retorno,id_material, rendimento))
    
    conexao.commit()
    print(f"Retorno atualizado com sucesso!\nRendimento do material: {rendimento:.2f}% e perda de {perda:.2f}%.\n")


        
 


menu()

conexao.close()

