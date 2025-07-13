from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")  # Можешь заменить на свою модель

class Input(BaseModel):
    texts: list[str]

@app.post("/embed")
def embed(input: Input):
    vectors = model.encode(input.texts).tolist()
    return {"vectors": vectors}
