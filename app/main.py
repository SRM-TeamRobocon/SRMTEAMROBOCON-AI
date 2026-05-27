from embeddings.embedder import embed_query
from vectorstore.chroma_store import search
from ingestion.chunker import chunk_text, trim_front_matter
from ingestion.cleaner import clean_text
from ingestion.pdf_loader import extract_pdf_text
from embeddings.embedder import load_model, embed_chunks
if __name__ == "__main__":
    model = load_model()

    # raw = extract_pdf_text("data/raw/jain.pdf")
    # cleaned = clean_text(raw)
    # trimmed = trim_front_matter(cleaned)
    # chunks = chunk_text(trimmed)

    # embeddings = embed_chunks(model, chunks)

    query = embed_query(model, "What is mahavira?")
    results = search(query)

    for result in results:
        print(result,"\n")