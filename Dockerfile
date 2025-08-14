FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download model at build time
RUN python download_model.py

EXPOSE 7860

CMD ["python", "server.py"]
