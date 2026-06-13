📘 Python QA Assistant (RAG-based AI System)
🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering Assistant built using Python. It helps users ask natural language questions and get accurate answers using embeddings + vector search + LLM.

🧠 Features
🔍 Semantic search using embeddings
📚 Context-based question answering (RAG pipeline)
⚡ FastAPI backend for API endpoints
🤖 OpenAI-powered response generation
🧩 Modular architecture (easy to extend)
📄 CSV-based dataset support
🏗️ Project Structure
python-qa-assistant/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── rag_pipeline.py      # RAG logic (retrieval + generation)
│   ├── vectorstore.py      # Vector DB logic
│   ├── data_loader.py      # Load dataset
│
├── data/
│   └── Questions.csv       # Dataset (not uploaded if large)
│
├── requirements.txt
├── .env                    # API keys (NOT pushed to GitHub)
└── README.md
⚙️ Installation & Setup
1️⃣ Clone repository
git clone https://github.com/harishsaini1812/python-qa-assistant.git
cd python-qa-assistant
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Setup environment variables

Create a .env file in root directory:

OPENAI_API_KEY=your_api_key_here
5️⃣ Run the application
uvicorn app.main:app --reload
📡 API Endpoints
🔹 Root
GET /
🔹 Ask Question
POST /ask

Request:

{
  "question": "What is Python?"
}

Response:

{
  "answer": "Python is a high-level programming language..."
}
🧪 Tech Stack
Python 🐍
FastAPI ⚡
OpenAI API 🤖
SentenceTransformers
FAISS / Vector DB
Pandas
🔐 Security Note
.env file is not included in repo
API keys should never be exposed publicly
Use environment variables for secrets
📈 Future Improvements
Add UI (React / Streamlit)
Use ChromaDB or Pinecone
Add chat history memory
Deploy on AWS / Render / Azure
👨‍💻 Author

Built by Harish Kumar Saini
