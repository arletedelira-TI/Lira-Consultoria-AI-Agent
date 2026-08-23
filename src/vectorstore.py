import os
from langchain_community.vectorstores import Chroma
from src.embeddings import get_embedding_model

VECTORSTORE_DIR = "vectorstore"

def create_or_update_vectorstore(chunks):
    """Cria ou atualiza o banco de vetores ChromaDB com os chunks fornecidos."""
    embeddings = get_embedding_model()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTORSTORE_DIR
    )
    return vectorstore

def load_vectorstore():
    """Carrega o banco de vetores existente."""
    embeddings = get_embedding_model()
    return Chroma(
        persist_directory=VECTORSTORE_DIR,
        embedding_function=embeddings
    )