from backend.vectorstore.chroma_store import search

def retrieve(query_embedding, top_k: int = 5) -> list[str]:
    """
    Retrieve similar chunks from Chroma based on query embedding.

    Args:
        query_embedding: The embedding vector for the query.
        top_k (int): Number of top similar chunks to retrieve.
    Returns:
        list[str]: List of retrieved chunk texts.
    """
    return search(query_embedding, top_k)
if __name__ == "__main__":
    try:
        from backend.embeddings.embedder import load_model, embed_query
    except ImportError as e:
        print(f"Error importing modules: {e}")
        exit(1)
        
    model = load_model()
    query = "What is the first chunk about?"
    query_embedding = embed_query(model, query)
    results = retrieve(query_embedding, top_k=5)
    print("Retrieved chunks:")
    for idx, chunk in enumerate(results):
        print(f"{idx + 1}. {chunk}")