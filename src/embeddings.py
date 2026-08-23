from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """Retorna o modelo de embeddings rodando 100% localmente na CPU."""

    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")