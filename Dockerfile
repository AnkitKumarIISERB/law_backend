# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install tiny build deps needed by some Python packages
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run expects the app to listen on this port
ENV PORT=8080
ENV PYTHONUNBUFFERED=1
EXPOSE 8080

# Start the app (keeps same entrypoint as your current app)
CMD ["python", "app.py"]
