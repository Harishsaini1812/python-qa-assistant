from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import generate_answer
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

app = FastAPI()

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
