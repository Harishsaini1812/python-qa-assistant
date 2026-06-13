from openai import OpenAI
import os
from app.vectorstore import VectorStore
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

vector_db = VectorStore()

def generate_answer(question: str):

    docs = vector_db.search(question)

    context = "\n\n".join(docs)

    prompt = f"""
You are a Python expert assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Give a clear and correct answer.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content