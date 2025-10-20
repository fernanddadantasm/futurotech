from flask_sqlalchemy import SQLAlchemy

# Apenas cria o objeto (SQLAlchemy), sem vinculá-lo ainda
db = SQLAlchemy()  

# Herda do SQLAlchemy, 'Model' que cria modelos ORM:
class Tarefas(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    # Usa Boolean para representar se a tarefa foi concluída
    concluida = db.Column(db.Boolean, nullable=False, default=False)
    data_criacao = db.Column(db.DateTime, default=db.func.now())
    prioridade = db.Column(db.String(20), default='normal')  # 'baixa', 'normal', 'alta'

    def __init__(self, titulo: str, descricao: str | None = None, concluida: bool = False):
        """Construtor explícito para ajudar o type-checker e facilitar
        criação de instâncias com kwargs (titulo, descricao, concluida).
        """
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        
