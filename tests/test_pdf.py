import pytest
from app.services.pdf_service import PDFService
from pathlib import Path

def test_pdf_extraction_and_chunking():
    file_path = "data/uploads/sample.pdf"
    if not Path(file_path).exists():
        pytest.skip("Sample PDF not found")
        
    text = PDFService.extract_text(file_path)
    assert isinstance(text, str)
    assert len(text) > 0

    chunks = PDFService.chunk_text(text, source="sample.pdf")
    assert len(chunks) > 0
    assert hasattr(chunks[0], "page_content")
    assert chunks[0].metadata["source"] == "sample.pdf"