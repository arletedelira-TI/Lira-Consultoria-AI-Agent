import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.vectorstore import load_vectorstore
from src.prompts import get_rag_prompt

load_dotenv()

def build_rag_chain():
    """Monta o pipeline RAG conectando a recuperação de dados ao LLM local."""
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # Aponta para o Ollama rodando localmente na sua máquina
    llm = Ollama(model="phi3", temperature=0.1)

    prompt = get_rag_prompt()
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain