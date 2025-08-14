FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirement files first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Hugging Face exposes $PORT
ENV PORT=7860

# Start your backend
CMD ["python", "app.py"]
