# 🧠 JustiFYI: Indian Law Assistant (Backend)

This is the **backend service** for *JustiFYI*, an AI-powered legal assistant.  
It performs **semantic search** over the **Bharatiya Nyaya Sanhita (BNS)** and generates **AI-powered explanations** via the **Groq API**, making Indian criminal law easier to understand.

---

## 📌 Features

- 🔍 **Semantic Search** using `sentence-transformers` to find the most relevant BNS sections  
- 🤖 **AI-generated explanations** via Groq’s `gemma2-9b-it` model  
- ⚡ **Precomputed embeddings** for fast legal lookups  
- 🔗 **REST API** endpoint powering the Flutter frontend  

---

## ⚙️ Tech Stack

- **Python 3 · Flask (REST API)**  
- **Hugging Face `sentence-transformers`**  
- **scikit-learn** (`cosine_similarity`)  
- **Groq API** (LLM inference)  
- **Pickle / NumPy** (for embedding storage)

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

## 🚀 Live Deployment

🚀 **Backend API (Hugging Face):** [JustiFYI Backend](https://huggingface.co/spaces/ankitkumariiserb/legal_chatbot_backend)  
📱 **Frontend App:** [JustiFYI Frontend](https://huggingface.co/spaces/ankitkumariiserb/legal_chatbot_frontend)  

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

## 🧠 How It Works

1️⃣ User enters a legal question (e.g., “What is the punishment for theft?”)
2️⃣ The backend finds the most relevant BNS section using semantic search
3️⃣ The Groq API explains the section in simple, plain language

---

## 🔗 Related Repository

👉 https://github.com/AnkitKumarIISERB/law_frontend

---

## 📜 License

This project is licensed under the MIT License. 

---



