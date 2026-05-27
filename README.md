# RAG Chatbot

A modular Retrieval-Augmented Generation (RAG) chatbot built with Python that ingests documents, converts them into semantic embeddings, stores them in a vector database, retrieves relevant context, and generates grounded responses using an LLM.

## Features

- PDF document ingestion
- Text cleaning and preprocessing
- Sentence-aware chunking with overlap
- Semantic embeddings using Sentence Transformers
- Persistent vector storage with ChromaDB
- Similarity-based retrieval
- Grounded prompt generation
- LLM integration
- Modular architecture
- Easy extensibility for multi-document support

## Project Structure

```bash
rag-chatbot/
│
├── app/
│   └── main.py
│
├── data/
│   └── raw/
│       └── document.pdf
│
├── ingestion/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── cleaner.py
│   └── chunker.py
│
├── embeddings/
│   ├── __init__.py
│   └── embedder.py
│
├── vectorstore/
│   ├── __init__.py
│   └── chroma_store.py
│
├── generation/
│   ├── __init__.py
│   ├── prompt_builder.py
│   └── llm_client.py
│
├── retrieval/
│
├── services/
│
├── chroma_db/
│
├── .env
├── .gitignore
└── ingest.py
```

## Architecture

### 1. Document Ingestion

Extract text from PDF documents.

```text
PDF → Raw Text
```

Handled by:

```python
ingestion/pdf_loader.py
```

---

### 2. Text Cleaning

Preprocess extracted text by:

- removing page numbers
- trimming whitespace
- normalizing formatting
- optional front matter cleanup

```text
Raw Text → Clean Text
```

Handled by:

```python
ingestion/cleaner.py
```

---

### 3. Chunking

Split cleaned text into overlapping semantic chunks.

Example:

```text
Chunk 1: Sentences 1–10
Chunk 2: Sentences 9–18
```

Handled by:

```python
ingestion/chunker.py
```

---

### 4. Embedding Generation

Convert chunks into vector embeddings.

```text
Text → Vector Embeddings
```

Handled by:

```python
embeddings/embedder.py
```

Default embedding model:

```text
all-MiniLM-L6-v2
```

---

### 5. Vector Storage

Store embeddings and source chunks in ChromaDB.

Stored data includes:

- chunk IDs
- chunk text
- embeddings

Handled by:

```python
vectorstore/chroma_store.py
```

---

### 6. Retrieval

User queries are embedded and matched against stored vectors.

```text
User Query
→ Query Embedding
→ Similarity Search
→ Top-K Relevant Chunks
```

Handled by:

```python
retrieval/retriever.py
```

---

### 7. Prompt Building

Inject retrieved chunks into a grounded prompt.

Example:

```text
Context:
[retrieved chunks]

Question:
[user query]

Instructions:
Answer only using the provided context.
If the answer is not found, explicitly say so.
```

Handled by:

```python
generation/prompt_builder.py
```

---

### 8. Response Generation

Send the grounded prompt to an LLM.

Handled by:

```python
generation/llm_client.py
```

---

### 9. Chat Service Orchestration

Coordinates the complete RAG pipeline.

Flow:

```text
User Query
→ Embed Query
→ Search Vector Store
→ Retrieve Chunks
→ Build Prompt
→ Generate LLM Response
```

Handled by:

```python
services/chat_service.py
```

---

## End-to-End Flow

```text
User uploads document
        ↓
PDF text extraction
        ↓
Text cleaning
        ↓
Chunking with overlap
        ↓
Embedding generation
        ↓
Store vectors in ChromaDB
        ↓
--------------------------------
        ↓
User asks question
        ↓
Embed user query
        ↓
Similarity search
        ↓
Retrieve relevant chunks
        ↓
Prompt construction
        ↓
LLM generation
        ↓
Final grounded response
```

## Tech Stack

### Core

- Python 3.10+

### Libraries

- PyMuPDF
- NLTK
- Sentence Transformers
- ChromaDB
- python-dotenv

### LLM Support

Compatible with:

- Google Gemini
- Groq
- OpenAI
- Claude
- Any API-based LLM

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
```

Create virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate
```

Install dependencies:

```bash
pip install pymupdf nltk sentence-transformers chromadb python-dotenv
```

Download NLTK tokenizer resources:

```bash
python
```

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
exit()
```

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=your_llm_api_key
```

Examples:

- Gemini API Key
- Groq API Key
- OpenAI API Key

## Running the Project

### Step 1: Ingest Documents

Run:

```bash
python -m vectorstore.chroma_store
```

This will:

- extract PDF text
- clean the text
- chunk the content
- generate embeddings
- store vectors in ChromaDB

---

### Step 2: Run Chatbot

```bash
python -m app.main
```

## Example Query

```text
What is Retrieval-Augmented Generation?
```

Example response:

```text
Retrieval-Augmented Generation (RAG) is a framework where relevant information is first retrieved from an external knowledge source and then supplied to a language model to generate grounded responses.
```

## Design Principles

This project follows:

- Separation of Concerns
- Single Responsibility Principle
- Modular Design
- Reusable Components
- MVP-first development
- Scalable architecture

## Future Improvements

Potential enhancements:

- FastAPI REST API
- interactive chatbot UI
- document upload support
- multi-document ingestion
- metadata filtering
- reranking
- hybrid search (BM25 + vector search)
- query rewriting
- conversation memory
- source citations
- authentication
- evaluation pipeline
- streaming responses
- Docker deployment

## License

MIT License