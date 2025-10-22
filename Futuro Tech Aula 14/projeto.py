import streamlit as st

st.title("Projeto Básico de CRUD com Streamlit")

# st.session_state para armazenar tarefas em memória 
if "lista_tarefas" not in st.session_state:
    st.session_state.lista_tarefas = []

def criar_tarefa(descricao, status):
    tarefa = {
        'descricao': descricao,
        'status': status,
        'id': len(st.session_state.lista_tarefas) + 1 
    }
    st.session_state.lista_tarefas.append(tarefa)
    st.success(f"Tarefa '{descricao}' criada com sucesso!")
    st.balloons()

def listar_tarefas():
    if st.session_state.lista_tarefas:
        for t in st.session_state.lista_tarefas:
            st.write(f"- {t['descricao']} (Status: {t['status']})")
    else:
        st.info("Nenhuma tarefa cadastrada.")

def atualizar_tarefa(descricao, status):
    for t in st.session_state.lista_tarefas:
        if t['descricao'] == descricao:
            t['status'] = status
            st.success(f"Tarefa '{descricao}' atualizada com sucesso!")
            return
    st.error(f"Tarefa '{descricao}' não encontrada.")

def deletar_tarefa(descricao):
    for t in st.session_state.lista_tarefas:
        if t['descricao'] == descricao:
            st.session_state.lista_tarefas.remove(t)
            st.success(f"Tarefa '{descricao}' deletada com sucesso!")
            return
    st.error(f"Tarefa '{descricao}' não encontrada.")

# Interface do usuário
st.header("Gerenciamento de Tarefas")
selecao = st.selectbox("Selecione a ação", ["Criar", "Listar", "Atualizar", "Deletar"])

match selecao:
    case "Criar":
        descricao = st.text_input("Descrição da Tarefa")
        status = st.selectbox("Status", ["Pendente", "Concluído"])
        if st.button("Criar Tarefa"):
            criar_tarefa(descricao, status)

    case "Listar":
        listar_tarefas()

    case "Atualizar":
        descricao = st.text_input("Descrição da Tarefa")
        status = st.selectbox("Status", ["Pendente", "Concluído"])
        if st.button("Atualizar Tarefa"):
            atualizar_tarefa(descricao, status)

    case "Deletar":
        descricao = st.text_input("Descrição da Tarefa")
        if st.button("Deletar Tarefa"):
            deletar_tarefa(descricao)

    case _:
        st.warning("Opção inválida.")
