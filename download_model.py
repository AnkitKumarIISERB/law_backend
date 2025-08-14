from sentence_transformers import SentenceTransformer

# Download and save model locally
model = SentenceTransformer("all-MiniLM-L6-v2")
model.save("model")

print("✅ Model downloaded and saved to 'model/' folder.")
