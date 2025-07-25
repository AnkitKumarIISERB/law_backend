from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import requests
import pickle
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)




with open("bns.txt", "r", encoding="utf-8") as f:
    bns_sections = f.read().split("\n")

EMBEDDING_FILE = "bns_embeddings.pkl"
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

if os.path.exists(EMBEDDING_FILE):
    with open(EMBEDDING_FILE, "rb") as f:
        section_embeddings = np.array(pickle.load(f))  
else:
    section_embeddings = embedding_model.encode(bns_sections, show_progress_bar=True)
    section_embeddings = np.array(section_embeddings)  
    with open(EMBEDDING_FILE, "wb") as f:
        pickle.dump(section_embeddings, f)



# GROQ API Info
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


def get_most_relevant_section(query):
    query_embedding = embedding_model.encode([query])
    similarities = cosine_similarity(query_embedding, section_embeddings)[0]
    top_idx = np.argmax(similarities)
    return bns_sections[top_idx]


def ask_groq(context, query):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gemma2-9b-it",
        "messages": [
            {"role": "system", "content": "You are a legal assistant who explains Indian law clearly using given legal text."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error fetching answer: {str(e)}"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    context = get_most_relevant_section(query)
    answer = ask_groq(context, query)

    return jsonify({
        "section": context,
        "answer": answer
    })


if __name__ == "__main__":
    app.run(port=5000)
