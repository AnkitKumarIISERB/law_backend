import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    print(f"🚀 Starting Flask server on 0.0.0.0:{port} ...")
    print("✅ Ready to receive requests at /ask")
    app.run(host="0.0.0.0", port=port)
