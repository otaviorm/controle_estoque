import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor =  conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    peso REAL NOT NULL,
    preco REAL NOT NULL
)
""")
conexao.commit()

def cadastrar_material():
    nome = input("Informe o material: ")
    tipo = input("Informe o tipo de material? (Bruto ou processado): ")
    peso = float(input("Informe o peso do material (kg): "))
    preco = float(input("Informe o preço do material (Em kg ou por unidade)?: "))
    cursor.execute("INSERT INTO materiais (nome, tipo, peso, preco) VALUES (?, ?, ?, ?)", (nome, tipo, peso, preco))

    conexao.commit()
    print("Material cadastrado com sucesso!")

cadastrar_material()
conexao.close()

# print("VSCode e ambiente virtual configurados com sucesso!")