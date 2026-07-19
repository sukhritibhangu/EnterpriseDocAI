from app.services.vector_service import VectorService
from app.services.llm_service import LLMService


class QAService:


    @staticmethod
    def ask(question):

        # 1. Retrieve relevant chunks
        chunks = VectorService.search(
            question,
            top_k=3
        )


        # 2. Combine chunks into context
        context = "\n\n".join([chunk["content"] for chunk in chunks])


        # 3. Generate answer using Groq
        answer = LLMService.generate_answer(
            context,
            question
        )


        return {"answer": answer, "sources": chunks}