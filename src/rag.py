import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Imports atualizados e unificados para LangChain 0.3+
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from src.vectorstore import load_vectorstore
from src.prompts import get_rag_prompt

load_dotenv()

def build_rag_chain():
    """Monta o pipeline RAG conectando a recuperação de dados ao LLM na nuvem (Gemini)."""
    print("Carregando vectorstore...")
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    print("Conectando ao Google Gemini...")
    # Usamos o gemini-1.5-flash, que é rápido, gratuito para uso de desenvolvimento e ideal para chat RAG
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.1,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    print("Montando prompt e correntes RAG...")
    prompt = get_rag_prompt()
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    print("Cadeia RAG pronta com sucesso na nuvem!")
    return rag_chain