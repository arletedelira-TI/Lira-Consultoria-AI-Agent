import streamlit as st
import os
from dotenv import load_dotenv
from src.rag import build_rag_chain

load_dotenv()

st.set_page_config(
    page_title="Lira Consultoria - Suporte Inteligente",
    page_icon="🏢",
    layout="centered"
)

# Faz cache do pipeline para não recarregar o modelo a cada nova mensagem
@st.cache_resource
def get_chain():
    return build_rag_chain()

st.title("🏢 Lira Consultoria")
st.subheader("Atendimento Institucional & Engenharia Oracle DB")

tab1, tab2, tab3 = st.tabs(["ℹ️ Sobre a Empresa", "📞 Serviços & Contato", "🤖 Suporte Nível 2"])

with tab1:
    st.markdown("### Institucional")
    st.write(
        "A **Lira Consultoria** é referência em sustentação de infraestrutura, "
        "otimização de queries (Tuning), licenciamento, sizing e suporte especializado em ambientes Oracle."
    )

with tab2:
    st.markdown("### Canais de Atendimento")
    st.write("**Horário:** Segunda a Sexta, das 08h às 18h")
    st.write("**E-mail comercial:** contato@liraconsultoria.com.br")
    st.write("**Plantão Crítico:** Acionamento via contrato de sustentação 24/7.")

with tab3:
    st.markdown("### Base de Conhecimento e Suporte")

    # Inicializa o histórico do chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe as mensagens anteriores
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Captura o input do usuário
    if user_input := st.chat_input("Dúvidas sobre erros ORA-, licenciamento ou sizing?"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Consultando a documentação oficial da Lira..."):
                try:
                    chain = get_chain()
                    res = chain.invoke({"input": user_input})
                    answer = res["answer"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Erro ao processar a resposta. Verifique seu token e a conexão: {e}")