# Use lightweight Python base
FROM python:3.10-slim

# Prevent Python from buffering stdout
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the default Hugging Face port
EXPOSE 7860

# Start the Flask app
CMD ["python", "server.py"]
