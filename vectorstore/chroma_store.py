import chromadb


# Persistent client
client = chromadb.PersistentClient(path="chroma_db")

# Create or get collection
collection = client.get_or_create_collection(name="jain_knowledge")


def store_chunks(chunks: list[str], embeddings) -> bool:
    """
    Store chunk text + embeddings in Chroma
    """

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print(f"Stored {len(chunks)} chunks in Chroma.")
    return True


def search(query_embedding, top_k: int = 5) -> list[str]:
    """
    Search similar chunks
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]

if __name__ == "__main__":
    try:
        client.reset()  # Clear existing data for testing
        print("Chroma database reset successfully.")
    except Exception as e:        print(f"Error resetting Chroma database: {e}")
    try:
        from embeddings.embedder import load_model, embed_chunks, embed_query
        from ingestion.chunker import chunk_text
        from ingestion.cleaner import clean_text
        from ingestion.pdf_loader import extract_pdf_text
    except ImportError as e:
        print(f"Error importing modules: {e}")
        exit(1)
        
    model = load_model()

    raw = extract_pdf_text("data/raw/jain.pdf")
    cleaned = clean_text(raw)
    chunks = chunk_text(cleaned)

    embeddings = embed_chunks(model, chunks)

    store_chunks(chunks, embeddings)

    query = embed_query(model, "What is moksha?")
    results = search(query)

    print(results)