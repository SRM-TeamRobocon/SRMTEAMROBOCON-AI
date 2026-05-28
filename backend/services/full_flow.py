from backend.embeddings.embedder import embed_query, load_model
from backend.generation.llm_client import generate_response
from backend.generation.prompt_builder import generate_prompt
from backend.retrival.retriver import retrieve


def full_flow(query: str) -> str:
    """
    Full flow: Embed query -> Retrieve similar chunks -> Generate response
    """
    model = load_model()
    query_embedding = embed_query(model, query)
    retrieved_chunks = retrieve(query_embedding, top_k=5)

    # `generate_prompt` expects context chunks first, then the user question.
    prompt = generate_prompt(retrieved_chunks, query)
    response = generate_response(prompt)
    return response


if __name__ == "__main__":
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting the program.")
            break
        response = full_flow(query)
        print("Response:")
        print(response)
