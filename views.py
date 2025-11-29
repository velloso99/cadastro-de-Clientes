# Importando banco de dados
import sqlite3

# Criando conexão
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")
#######################################################################################################
#Tabela de Bairros_____________________________________
def criar_bairro(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO bairro (BAIRRO) values(?)"
        cur.execute(query, i)
#Deletar Bairro
def deletar_bairro(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM bairro WHERE id=? "
        cur.execute(query, i)