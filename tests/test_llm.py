import pytest
from app.services.llm_service import LLMService

def test_llm_service():
    context = "Python is used for AI and Machine Learning."
    question = "What is Python used for?"
    
    answer = LLMService.generate_answer(context, question)
    
    assert isinstance(answer, str)
    assert len(answer) > 0