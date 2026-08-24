# Lira Consultoria AI Agent — Challenge Oracle ONE / Alura

Assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** desenvolvido para o **Challenge Oracle ONE**, em parceria com a **Alura**.

O projeto tem como objetivo fornecer suporte e consultoria técnica especializada em **banco de dados e ecossistema Oracle**, utilizando Inteligência Artificial para consultar documentações técnicas de forma rápida e contextualizada.

---

## 🏗️ Arquitetura da Solução

O fluxo da aplicação RAG funciona em etapas integradas:

1. **Ingestão de Documentos:** os arquivos PDF armazenados na pasta `data/` são carregados utilizando `PyPDF` e divididos em trechos menores com `RecursiveCharacterTextSplitter`.

2. **Geração de Embeddings:** os trechos de texto são transformados em vetores numéricos utilizando o modelo de embeddings da API do Google Gemini.

3. **Armazenamento Vetorial:** os vetores são indexados e armazenados localmente utilizando o **ChromaDB**.

4. **Recuperação e Resposta (RAG):** quando o usuário realiza uma pergunta através do **Streamlit**, o sistema busca os trechos mais relevantes no ChromaDB e os envia ao modelo **Google Gemini** para gerar uma resposta contextualizada.

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3.11** — linguagem principal
* **Streamlit** — interface web interativa
* **LangChain** — orquestração do pipeline RAG
* **Google Gemini API** — geração de respostas e embeddings
* **ChromaDB** — banco de dados vetorial
* **PyPDF** — extração de texto de documentos PDF

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Lira-Consultoria-AI-Agent.git
cd Lira-Consultoria-AI-Agent
```

### 2. Criar e ativar o ambiente virtual

No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a variável de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google Gemini:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

> **Importante:** não compartilhe sua chave de API e não envie o arquivo `.env` para o GitHub.

### 5. Adicionar os documentos

Coloque os arquivos PDF de documentação técnica na pasta:

```text
data/
```

Em seguida, execute o processo de ingestão para gerar o banco vetorial:

```bash
PYTHONPATH=. python src/vectorstore.py
```

### 6. Iniciar a aplicação

Execute o Streamlit:

```bash
streamlit run app.py
```

A aplicação estará disponível no endereço local apresentado pelo Streamlit.

---

## 💡 Exemplos de Perguntas

O agente pode responder perguntas técnicas relacionadas à documentação fornecida, como:

* *Como posso otimizar uma consulta SQL lenta em bancos de dados Oracle?*
* *Quais são as melhores práticas para criação de índices no Oracle Database?*
* *Como funciona o particionamento de tabelas no Oracle?*
* *Quais ferramentas podem ser utilizadas para analisar o desempenho de uma consulta?*

---

## 🤖 Exemplo de Interação

**Pergunta:**

> Como posso otimizar uma consulta SQL lenta em bancos de dados Oracle?

**Resposta esperada:**

> Com base na documentação técnica fornecida, a otimização de consultas lentas no Oracle pode envolver a análise do plano de execução, identificação de gargalos, criação de índices adequados, atualização das estatísticas utilizando `DBMS_STATS` e, quando necessário, utilização de hints para orientar o otimizador.

---

## 🎯 Objetivo do Projeto

Este projeto demonstra a aplicação prática de **Inteligência Artificial Generativa, RAG, bancos de dados vetoriais e processamento de documentos** para solucionar um problema real: transformar um grande volume de documentação técnica em uma fonte de conhecimento consultável por meio de linguagem natural.

---
## 🎯 Criado por:
Arlete de Lira