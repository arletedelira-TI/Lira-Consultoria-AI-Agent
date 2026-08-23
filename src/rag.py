import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.vectorstore import load_vectorstore
from src.prompts import get_rag_prompt

load_dotenv()

def build_rag_chain():
    """Monta o pipeline RAG conectando a recuperação de dados ao LLM local."""
    print("Carregando vectorstore...")
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    print("Conectando ao Ollama (Phi-3)...")
    llm = OllamaLLM(model="phi3", temperature=0.1)

    print("Montando prompt e correntes RAG...")
    prompt = get_rag_prompt()
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    print("Cadeia RAG pronta com sucesso!")
    return rag_chain