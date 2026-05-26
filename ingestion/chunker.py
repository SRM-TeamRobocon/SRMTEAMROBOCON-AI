import nltk
from nltk.tokenize import sent_tokenize

# Run once if punkt not downloaded
#nltk.download('punkt')

def chunk_text(clean_text: str, chunk_size: int = 10, overlap: int = 2) -> list[str]:
    """
    Splits cleaned text into overlapping sentence-based chunks.

    Args:
        clean_text (str): Preprocessed text
        chunk_size (int): Number of sentences per chunk
        overlap (int): Number of overlapping sentences

    Returns:
        list[str]: List of chunked text strings
    """

    sentences = sent_tokenize(clean_text)

    if not sentences:
        return []

    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(sentences), step):
        chunk = sentences[i:i + chunk_size]

        if not chunk:
            continue

        chunks.append(" ".join(chunk))

    print(f"Created {len(chunks)} chunks.")
    return chunks


# Testing
if __name__ == "__main__":
    from cleaner import clean_text
    from pdf_loader import extract_pdf_text

    raw_text = extract_pdf_text("../data/raw/jain.pdf")
    cleaned = clean_text(raw_text)
    chunks = chunk_text(cleaned)

    print(chunks[20])  # Print the first chunk for verification