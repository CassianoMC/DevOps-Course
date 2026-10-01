import sqlite3

# CREATE --> Criação de tabela e inserção de dados de exemplo
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Contatos")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Contatos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
email TEXT,
telefone TEXT
)
""")
conn.commit()

dados_exemplo = [
    ('João', 'joao@email.com', '1234-5678'),
    ('Maria', 'maria@email.com', '1111-2222'),
    ('Carlos', 'carlos@email.com', '3333-4444')
    ]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

# READ --> Leitura e exibição dos contatos
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()

for contato in contatos:
    print(contato)

# UPDATE --> Atualização do numero de telefone do contato com ID 2
novo_telefone = '9999-9999'
contato_id = 2

cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
print(f"\nO telefone da pessoa com ID: {contato_id}, foi atulizado para: {novo_telefone}")
conn.commit()

# DELETE --> Exclusão do contato com ID 1
contato_id_para_excluir = 1

cursor.execute('DELETE FROM Contatos WHERE id =?', (contato_id_para_excluir,))
conn.commit()

# Fechando Conexão
conn.close()