import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import CHUNK_SIZE, CHUNK_OVERLAP


class PDFService:
    """Handles PDF extraction and chunking."""

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        doc = fitz.open(pdf_path)

        text = ""

        for page in doc:
            # ensure we always get a string representation of the page text
            text += page.get_text("text")

        doc.close()

        return text

    @staticmethod
    def chunk_text(text: str, source: str = "Unknown"):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        return splitter.create_documents([text], metadatas=[{"source": source}])