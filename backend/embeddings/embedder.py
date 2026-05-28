from sentence_transformers import SentenceTransformer

def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(model, chunks):
    return model.encode(chunks)


def embed_query(model, query):
    return model.encode(query)

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully.") 
    # Example usage    chunks = ["This is the first chunk.", "This is the second chunk."]
    query = "What is the first chunk about?"
    query_embedding = embed_query(model, query)
    print(query_embedding)
    print("Query embedding generated successfully.")    