# 🧠 Law Assistant Backend (Flask + Groq + Sentence Transformers)

This is the backend for a legal assistant application built with Flask and powered by Groq's large language models. It uses sentence embeddings to retrieve the most relevant legal section from Indian law and generates a human-friendly explanation using an LLM.

---

## 🚀 Features

- 🧾 Semantic search over Indian legal sections (BNS)
- 🔗 Sentence embeddings with `sentence-transformers`
- 🧠 Answers generated via Groq's `gemma2-9b-it` LLM
- 🔒 `.env`-based API key configuration
- 🔥 Flask + CORS support for smooth frontend integration

---

## 🗂️ Project Structure

law_backend/
├── app.py # Main Flask app
├── bns.txt # Legal sections (raw text)
├── bns_embeddings.pkl # Precomputed embeddings for fast search
├── generate_embeddings.ipynb # Colab notebook to generate embeddings
├── requirements.txt # Python dependencies
└── README.md # You're reading this!

---

## ⚙️ Environment Variables

Create a `.env` file in the root folder with your Groq API key:

env
GROQ_API_KEY=`your_groq_api_key_here`

---

## 📓 Embedding Generation

The embeddings (bns_embeddings.pkl) were created using the notebook generate_embeddings.ipynb. It uses the all-MiniLM-L6-v2 model from sentence-transformers to encode each section from bns.txt.

---

## 🧪 API Usage
POST /ask
Request Body:
{
  "query": "What is the punishment for theft?"
}
Response:
{
  "section": "Section text that is most relevant",
  "answer": "LLM-generated explanation based on section"
}

---

## 🧩 Dependencies
Install all required packages:
pip install -r requirements.txt

---

## 🛰️ Related Repositories
👉 https://github.com/AnkitKumarIISERB/law_frontend

---

## 📜 License
This project is licensed under the MIT License.

---





