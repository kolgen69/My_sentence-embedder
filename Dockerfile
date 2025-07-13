FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir sentence-transformers fastapi uvicorn

WORKDIR /app
COPY embed_server.py .

EXPOSE 8000

CMD ["uvicorn", "embed_server:app", "--host", "0.0.0.0", "--port", "8000"]
