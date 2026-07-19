import pytest
from app.services.pdf_service import PDFService
from app.services.vector_service import VectorService
from pathlib import Path

def test_vector_service():
    file_path = "data/uploads/sample.pdf"
    if not Path(file_path).exists():
        pytest.skip("Sample PDF not found")
        
    text = PDFService.extract_text(file_path)
    chunks = PDFService.chunk_text(text, source="sample.pdf")
    assert len(chunks) > 0
    
    # Check if add_documents works
    VectorService.add_documents(chunks)
    assert True # If no exception, it passes