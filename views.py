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
#Ver Bairros
def ver_bairro():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM bairro')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista
#Atualizar Bairro
def atualizar_bairro(i):

    with con:
        cur = con.cursor()
        query = "UPDATE bairro SET BAIRRO=? WHERE id=?"
        cur.execute(query, i)  # A variável 'dados' já é uma tupla
        con.commit()

        # Retorna True se a atualização for bem-sucedida
        return cur.rowcount > 1
#######################################################################################################
#Tabela Carteira de Clientes__________________________
def criar_cliente(i):   
    with con:
        cur = con.cursor()
        query = "INSERT INTO clientes (MATRICULA, RAZÃO SOCIAL, NOME FANTASIA, CNPJ, ENDREÇO, BAIRRO, CIDADE, ESTADO, ATENDENTE, TELEFONE) values(?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#Deletar Cliente
def deletar_cliente(i):  
    with con:
        cur = con.cursor()
        query = "DELETE FROM clientes WHERE id=? "
        cur.execute(query, i)           
#Ver Clientes
def ver_cliente():  
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM clientes')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista
#Atualizar Cliente
def atualizar_cliente(i):   
    with con:
        cur = con.cursor()
        query = "UPDATE clientes SET MATRICULA=?, RAZÃO SOCIAL=?, NOME FANTASIA=?, CNPJ=?, ENDREÇO=?, BAIRRO=?, CIDADE=?, ESTADO=?, ATENDENTE=?, TELEFONE=? WHERE id=?"
        cur.execute(query, i)  # A variável 'dados' já é uma tupla
        con.commit()

        # Retorna True se a atualização for bem-sucedida
        return cur.rowcount > 0
