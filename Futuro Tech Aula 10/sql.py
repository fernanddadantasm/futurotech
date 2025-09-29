strings_sql = {
"criar_tabela_clientes" :
"""
    CREATE TABLE IF NOT EXISTS Clientes (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) UNIQUE,
    ativo INTEGER
);
""",
"inserir_cliente" : "INSERT INTO Clientes (nome, cpf, ativo) VALUES (?, ?, ?);",
"alterar_nome_cliente": "UPDATE Clientes SET nome = ?  WHERE codigo = ?",
"excluir_cliente":  "DELETE FROM Clientes WHERE codigo = ?", 
}
