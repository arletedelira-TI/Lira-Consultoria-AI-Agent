# Lira Consultoria - Assistente RAG para Suporte Técnico Oracle

> Projeto desenvolvido para o desafio **Oracle Next Education (ONE)** em parceria com a **Alura**, utilizando **Inteligência Artificial Generativa** e a arquitetura **Retrieval-Augmented Generation (RAG)** para responder consultas técnicas sobre produtos Oracle a partir de uma base de conhecimento vetorial.

---

## 📖 Sobre o Projeto

Este projeto nasceu de uma experiência pessoal.

Durante três anos atuei como **Solution Engineer na Oracle**, trabalhando com consultoria técnica e pré-vendas para soluções de Banco de Dados. Um dos maiores desafios da função era navegar por uma grande quantidade de documentação técnica e regras de licenciamento para responder rapidamente às necessidades de clientes e equipes comerciais.

Com o conhecimento adquirido no programa **Oracle Next Education**, desenvolvi este assistente para demonstrar como a IA Generativa pode transformar documentação técnica em uma base de conhecimento pesquisável, oferecendo respostas contextualizadas por meio da arquitetura **RAG**.

---

## 🚀 Tecnologias

* Python 3.12
* Streamlit
* LangChain
* ChromaDB
* Sentence Transformers (`all-MiniLM-L6-v2`)
* Ollama
* Microsoft Phi-3
* Oracle Cloud Infrastructure (OCI)

---

## 🏗 Arquitetura

```text
Usuário
   │
   ▼
Streamlit
   │
   ▼
Pipeline RAG (LangChain)
   │
   ├── Retriever (ChromaDB)
   └── LLM (Phi-3 via Ollama)
   │
   ▼
Resposta contextualizada
```

---

## 📂 Estrutura do Projeto

```text
LIRA-CONSULTORIA-AGENT/
├── data/                  # Base de conhecimento (PDFs)
├── src/
│   ├── embeddings.py
│   ├── prompts.py
│   ├── rag.py
│   └── vectorstore.py
├── vectorstore/           # Banco vetorial persistido
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/LIRA-CONSULTORIA-AGENT.git

cd LIRA-CONSULTORIA-AGENT

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt

# Baixe o modelo
ollama pull phi3

# Execute a aplicação
streamlit run app.py
```

---

## 💡 Como Funciona

1. A documentação técnica é convertida em embeddings.
2. Os vetores são armazenados no **ChromaDB**.
3. A pergunta do usuário é comparada com a base vetorial.
4. Os documentos mais relevantes são recuperados.
5. O modelo **Phi-3** gera uma resposta utilizando o contexto.

---

## ✨ Diferenciais

* Arquitetura **RAG** executada localmente.
* Sem dependência de APIs pagas.
* Banco vetorial persistente com ChromaDB.
* Embeddings gerados com Sentence Transformers.
* Estrutura modular para expansão da base de conhecimento.
* Base composta por documentação Oracle e materiais internos da consultoria.

---

## 🎯 Objetivo

Este projeto demonstra a aplicação prática de IA Generativa para resolver um problema real: facilitar o acesso ao conhecimento técnico em ambientes com grande volume de documentação, unindo minha experiência profissional na Oracle aos conhecimentos adquiridos durante o **Oracle Next Education (ONE)**.

---

## 👩‍💻 Autora

**Arlete**

Ex-Solution Engineer na Oracle, com experiência em consultoria técnica e pré-vendas para soluções de Banco de Dados. Atualmente direcionando a carreira para Inteligência Artificial, Data Science e Computação em Nuvem por meio do programa **Oracle Next Education (ONE)**.

---

## 📄 Licença

Projeto desenvolvido para fins educacionais como parte do desafio **Oracle Next Education (ONE)** em parceria com a **Alura**.
