#  Controle de Estoque para Materiais Processados

Este é um sistema simples de **Controle de Estoque** desenvolvido em **Python** com uso de banco de dados **SQLite**. Ele permite cadastrar materiais, consultar históricos de entrada e saída, e pesquisar por responsável ou data de movimentação do material.

##  Funcionalidades

-  Cadastro de materiais (nome, tipo, peso, preço, responsável, data de saída, data de retorno)
-  Listagem completa dos cadastros registrados
-  Pesquisa de materiais por responsável ou por data de saída
-  Armazenamento em banco de dados SQLite (`estoque.db`)

##  Tecnologias utilizadas

- **Python 3**
- **SQLite3** (banco de dados local)

## ▶ Como usar

### 1. Clone o repositório:

```bash
git clone https://github.com/otaviorm/controle-estoque.git
cd controle-estoque
python app.py
