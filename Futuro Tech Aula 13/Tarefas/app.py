from flask import ( Flask, )    # Importa o Módulo principal do Flask
from modelos import ( db, )      # Importa o db daqui
from routes.tarefas import ( rotas_tarefas, )
import os

app = Flask(__name__)

# Caminho absoluto para o banco:
pasta = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(pasta, "tarefas.db")}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Futuro Tech"

# Agora inicializa o db dentro do app
db.init_app(app)

# registra blueprint (Gernciamento de Rotas):
app.register_blueprint(rotas_tarefas)

# Cria um contexto para esta aplicação (para o Flask saber
#  que o banco pertence a esta e não a outras app Flask)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)