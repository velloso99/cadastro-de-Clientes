#Importar banco de dados
import sqlite3

# Criando conexão
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco e Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")

# Criando tabelas do Banco de Dados
#Tabela Carteira de Clientes__________________________
try:
    with con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                MATRICULA NUMERIC,
                RAZÃO SOCIAL TEXT,
                NOME FANTASIA TEXT,
                CNPJ NUMERIC,   
                ENDREÇO TEXT,
                BAIRRO TEXT,
                CIDADE TEXT,
                ESTADO TEXT,
                ATENDENTE TEXT,
                TELEFONE NUMERIC,
                    
                foreign key (BAIRRO) references bairros(BAIRRO) on update cascade on delete cascade
                )""")
        print("Tabela de clientes criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de clientes!")

# Tabela de Bairros_____________________________________
try:
    with con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS bairro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                BAIRRO TEXT
                )""")
        print("Tabela de bairros criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de bairros!")