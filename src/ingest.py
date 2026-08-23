import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vectorstore import create_or_update_vectorstore

def run_ingestion():
    """Lê PDFs, divide em chunks e salva no ChromaDB."""
    print("Iniciando varredura recursiva de arquivos PDF em 'data/'...")
    
    # O PyPDFDirectoryLoader já busca documentos em subpastas automaticamente
    loader = PyPDFDirectoryLoader("data/")
    documents = loader.load()

    if not documents:
        print("Nenhum documento PDF encontrado na estrutura de 'data/'.")
        return

    print(f"Total de páginas carregadas das subpastas: {len(documents)}")

    # Quebra de texto otimizada para manter o contexto técnico
    splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=150)
    chunks = splitter.split_documents(documents)
    print(f"Total de chunks gerados: {len(chunks)}")

    print("Indexando vetores no ChromaDB...")
    create_or_update_vectorstore(chunks)
    print("Processo concluído com sucesso! Banco vetorial atualizado em 'vectorstore/'.")

if __name__ == "__main__":
    run_ingestion()