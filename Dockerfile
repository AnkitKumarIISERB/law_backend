FROM python:3.10

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Workdir
WORKDIR /app

# Copy everything into the image
COPY . /app

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

# Spaces expose 7860
EXPOSE 7860

# Start your backend
CMD ["python", "app.py"]
