# Lira Consultoria AI Agent

> Assistente inteligente baseado em **Retrieval-Augmented Generation (RAG)** para consulta de documentação técnica Oracle, desenvolvido com **LangChain**, **ChromaDB** e **Large Language Models (LLMs)**.

Projeto desenvolvido durante o programa **Oracle Next Education (ONE)** em parceria com a **Alura**, com o objetivo de demonstrar a aplicação de IA Generativa na construção de assistentes especializados para suporte técnico.

---

# 📖 Sobre o Projeto

A motivação para este projeto surgiu da minha experiência profissional na **Oracle**, meu **primeiro emprego na área de tecnologia**, onde atuei como **Solution Engineer** por três anos.

Nesse período, trabalhei com consultoria técnica e pré-vendas para soluções de Banco de Dados, apoiando clientes e equipes comerciais na avaliação de arquiteturas, licenciamento e produtos Oracle. A rotina envolvia consultar uma extensa documentação técnica para localizar informações específicas e responder rapidamente a diferentes cenários de negócio.

Este projeto reproduz esse contexto por meio de uma arquitetura **RAG (Retrieval-Augmented Generation)**, permitindo que um modelo de linguagem consulte uma base vetorial construída a partir da documentação técnica antes de gerar uma resposta. O resultado é um assistente capaz de fornecer respostas contextualizadas, reduzindo alucinações e melhorando a precisão das informações.

Além de representar uma aplicação prática dos conhecimentos adquiridos no **Oracle Next Education (ONE)**, o projeto demonstra como técnicas modernas de IA podem ser utilizadas para organizar e disponibilizar conhecimento técnico de forma eficiente.

---

# 🚀 Tecnologias

* Python 3.12
* Streamlit
* LangChain
* ChromaDB
* Sentence Transformers (`all-MiniLM-L6-v2`)
* Ollama
* Microsoft Phi-3
* Oracle Cloud Infrastructure (OCI)

---

# 🌿 Versões do Projeto

O projeto possui duas implementações, adaptadas para diferentes cenários de execução.

## Branch `main`

Versão destinada à execução local.

**Stack utilizada:**

* Ollama
* Microsoft Phi-3
* ChromaDB
* LangChain
* Streamlit

**Características**

* Execução totalmente local.
* Não depende de APIs externas.
* Ideal para desenvolvimento, estudos e experimentação.

---

## Branch `cloud-version`

Versão preparada para implantação no **Streamlit Community Cloud**.

**Stack utilizada:**

* Google Gemini API
* ChromaDB
* LangChain
* Streamlit

**Características**

* Execução em nuvem.
* Configuração por meio de Secrets do Streamlit.
* Não requer instalação do Ollama.

---

# 🏗 Arquitetura

```text
                 Pergunta do usuário
                         │
                         ▼
                    Streamlit
                         │
                         ▼
                 Pipeline RAG
                 (LangChain)
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 Recuperação de contexto          Modelo de Linguagem
      (ChromaDB)             (Phi-3 ou Gemini)
          │                             │
          └──────────────┬──────────────┘
                         ▼
              Resposta contextualizada
```

---

# ⚙️ Funcionamento

1. A documentação técnica é processada e convertida em embeddings.
2. Os embeddings são armazenados no ChromaDB.
3. A pergunta do usuário é convertida em representação vetorial.
4. O retriever recupera os documentos semanticamente mais relevantes.
5. O contexto recuperado é enviado ao modelo de linguagem.
6. O modelo gera uma resposta fundamentada na documentação disponível.

---

# ✨ Principais Recursos

* Arquitetura **Retrieval-Augmented Generation (RAG)**.
* Base vetorial persistente com **ChromaDB**.
* Busca semântica utilizando **Sentence Transformers**.
* Interface web desenvolvida em **Streamlit**.
* Estrutura modular baseada em **LangChain**.
* Suporte para execução local ou em nuvem.
* Fácil expansão da base de conhecimento.

---

# 🎯 Objetivo

Demonstrar a aplicação prática de Inteligência Artificial Generativa em um cenário corporativo de suporte técnico, utilizando uma arquitetura RAG para transformar documentação Oracle em uma base de conhecimento consultável por linguagem natural.

O projeto também evidencia a integração entre recuperação de informação, bancos vetoriais e grandes modelos de linguagem na construção de assistentes especializados.

---

# 👩‍💻 Autora

**Arlete**

Profissional em transição para as áreas de Inteligência Artificial, Ciência de Dados e Computação em Nuvem.

Atuou como **Solution Engineer na Oracle**, seu primeiro cargo na área de tecnologia, adquirindo experiência em consultoria técnica, pré-vendas e soluções de Banco de Dados. Atualmente desenvolve projetos focados em IA Generativa, LLMs, arquiteturas RAG e Machine Learning.

linkedin:

---

# 📄 Licença

Projeto desenvolvido para fins educacionais como parte do programa **Oracle Next Education (ONE)** em parceria com a **Alura**.

