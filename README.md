# 🧠 Indian Law Q&A Backend

This is the backend service for a legal question-answering system. It uses semantic search to find the most relevant section from the **Bharatiya Nyaya Sanhita (BNS)** and generates AI-powered explanations using the **Groq API**.

---

## 📌 Features

- 🔍 Semantic search over Indian legal text using `sentence-transformers`
- 🤖 AI-generated explanations via Groq’s `gemma2-9b-it` model
- 🔗 REST API endpoint to serve responses to the frontend
- 🧠 Precomputed embeddings stored for fast lookup

---

## ⚙️ Tech Stack

- Python 3
- Flask (REST API)
- Hugging Face `sentence-transformers`
- scikit-learn (`cosine_similarity`)
- Groq API (LLM)
- Pickle (for saving embeddings)

---

## 🗂 Project Structure

law_backend/
│
├── app.py                     # Main Flask app
├── bns.txt                    # List of BNS sections (1 per line)
├── bns_embeddings.pkl         # Pickled numpy array of section embeddings
├── generate_embeddings.ipynb  # Notebook to generate and save embeddings
├── requirements.txt           # Python dependencies
├── .env                       # (Not committed) contains GROQ_API_KEY
└── render.yaml                # Optional: for Render.com deployment

---

## 🚀 Getting Started

1. Clone the repository
git clone https://github.com/AnkitKumarIISERB/law_backend.git
cd law_backend

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add your Groq API key
Create a .env file in the root folder:

GROQ_API_KEY=your_groq_api_key_here

🔐 Do NOT share your .env file or commit it to GitHub.

---

## 🧪 Run the API

python app.py

Your server will start at http://localhost:5000

---

## 📮 API Usage

POST /ask
Request JSON:

{
  "query": "What is the punishment for theft under Indian law?"
}

Response JSON:

{
  "section": "Section 303: Whoever commits theft shall be punished with...",
  
  "answer": "According to the Bharatiya Nyaya Sanhita, theft is punishable by..."
}

---

## 🧠 Embedding Generation

The generate_embeddings.ipynb Colab notebook loads bns.txt, computes sentence embeddings using the all-MiniLM-L6-v2 model, and saves them as bns_embeddings.pkl.

Run it once to generate/update your embeddings.

---

## 🔗 Related Repository

👉 https://github.com/AnkitKumarIISERB/law_frontend

---

## 📜 License

This project is licensed under the MIT License. 

---



