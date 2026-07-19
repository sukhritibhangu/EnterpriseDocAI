import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLMResponse:
    def __init__(self, content):
        self.content = content


class LLMService:

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    @staticmethod
    def generate_answer(context, question):

        prompt = f"""
You are an AI assistant for document analysis.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        response = LLMService.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


    @staticmethod
    def invoke(prompt):

        response = LLMService.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return LLMResponse(answer)


def get_llm():
    return LLMService