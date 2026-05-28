from backend.ingestion.chunker import chunk_text
from backend.ingestion.cleaner import clean_text
from backend.ingestion.pdf_loader import extract_pdf_text

def ingest_pdf(pdf_path: str) -> list[str]:
    """
    Ingests a PDF file and returns a list of cleaned, chunked text.

    Args:
        pdf_path (str): Path to the PDF file
    Returns:
        list[str]: List of cleaned, chunked text strings
    """  
    raw = extract_pdf_text(pdf_path)
    cleaned = clean_text(raw)
    chunks = chunk_text(cleaned)
    return chunks
  
