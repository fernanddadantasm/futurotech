from flask import ( Blueprint, render_template, request, redirect, url_for, flash )
from modelos import (db, Tarefas)  # importa do modelos, não do app

# Um 'Blueprint' é como um módulo de rotas:
# “Ei, Flask, pega todas as rotas defincodigoas dentro do objeto 'rotas_tarefas'
#   e adiciona no aplicativo principal.”
rotas_tarefas = Blueprint(name="tarefas", import_name=__name__)

# -----------------------------
# ROTA PRINCIPAL (READ)
# -----------------------------
@rotas_tarefas.route('/')
def principal():
    tarefas = Tarefas.query.order_by(Tarefas.codigo).all()
    # O render_template substitui a string SQL:
    return render_template('principal.html', tarefas=tarefas)


# -----------------------------
# CRIAR NOVA TAREFA (INSERT)
# -----------------------------
@rotas_tarefas.route("/inserir", methods=['GET', 'POST'])
def inserir_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form.get('descricao', '')

        if not titulo:
            # flash: O texto e a categoria da msg:
            flash('O título é obrigatório!', 'erro')
            return redirect( url_for("tarefas.inserir_tarefa") )

        nova_tarefa = Tarefas(titulo=titulo, descricao=descricao)
        # è o 'INSERT' do SQL:
        db.session.add(nova_tarefa)
        db.session.commit()
        # flash: O texto e a categoria da msg:
        flash('Tarefa inserida com sucesso!', 'sucesso')
        return redirect( url_for("tarefas.principal") )

    return render_template('inserir_tarefa.html')


# -----------------------------
# EDITAR TAREFA (UPDATE)
# -----------------------------
@rotas_tarefas.route('/alterar/<int:codigo>', methods=['GET', 'POST'])
def alterar_tarefa(codigo):
    tarefa = Tarefas.query.get_or_404(codigo)

    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form.get('descricao', '')
        # Tarefa é um dicionário que irá conter a chave 'concluida' -> True/False
        tarefa.concluida = "concluida" in request.form

        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'sucesso')
        return redirect( url_for("tarefas.principal") )

    return render_template("alterar_tarefa.html", tarefa=tarefa)


# -----------------------------
# DELETAR TAREFA (DELETE)
# -----------------------------
@rotas_tarefas.route('/excluir/<int:codigo>', methods=['POST'])
def excluir_tarefa(codigo):
    tarefa = Tarefas.query.get_or_404(codigo)
    db.session.delete(tarefa)
    db.session.commit()
    flash('Tarefa excluída!', 'sucesso')
    return redirect(url_for("tarefas.principal"))