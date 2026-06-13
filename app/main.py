from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import generate_answer

app = FastAPI()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

class Query(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(query: Query):
    answer = generate_answer(query.question)
    return {
        "question": query.question,
        "answer": answer
    }
