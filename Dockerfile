# Use Python 3.10 for maximum compatibility
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Render will use
EXPOSE 8000

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]
