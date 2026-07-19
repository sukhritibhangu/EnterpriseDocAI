import pytest
from app.services.vector_service import VectorService

def test_search():
    query = "What skills are required for DAA?"
    
    results = VectorService.search(query)
    
    assert isinstance(results, list)
    if len(results) > 0:
        assert isinstance(results[0], dict)
        assert "content" in results[0]
        assert "metadata" in results[0]