import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.embeddings import get_embedding_model

VECTORSTORE_DIR = "vectorstore"
DOCS_DIR = "data"  # Certifique-se de que seus PDFs estão numa pasta chamada 'docs' (ou ajuste o nome aqui)

def create_or_update_vectorstore(chunks):
    """Cria ou atualiza o banco de vetores ChromaDB com os chunks fornecidos."""
    embeddings = get_embedding_model()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTORSTORE_DIR
    )
    print(f"Vectorstore criado/atualizado com sucesso em '{VECTORSTORE_DIR}'!")
    return vectorstore

def load_vectorstore():
    """Carrega o banco de vetores existente."""
    embeddings = get_embedding_model()
    return Chroma(
        persist_directory=VECTORSTORE_DIR,
        embedding_function=embeddings
    )

if __name__ == "__main__":
    print("Iniciando o processo de ingestão de documentos...")
    
    # 1. Carregar os PDFs da pasta de documentos
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
        print(f"A pasta '{DOCS_DIR}' não existia e foi criada. Coloque seus PDFs nela e execute novamente.")
    else:
        loader = PyPDFDirectoryLoader(DOCS_DIR)
        documents = loader.load()
        
        if not documents:
            print(f"Nenhum documento PDF encontrado na pasta '{DOCS_DIR}'.")
        else:
            print(f"{len(documents)} páginas carregadas com sucesso.")
            
            # 2. Dividir os documentos em chunks (pedaços menores)
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_documents(documents)
            print(f"Total de chunks gerados: {len(chunks)}")
            
            # 3. Criar e persistir o vectorstore
            create_or_update_vectorstore(chunks)