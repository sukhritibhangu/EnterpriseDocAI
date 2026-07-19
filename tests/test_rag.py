import pytest
from app.services.rag_service import QAService

def test_qa_service():
    question = "What skills are required for internship?"
    
    result = QAService.ask(question)
    
    assert isinstance(result, dict)
    assert "answer" in result
    assert "sources" in result
    assert isinstance(result["answer"], str)
    assert isinstance(result["sources"], list)