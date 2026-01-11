from fastapi import FastAPI
from backend.services.pipeline import analyze_articles

app = FastAPI(
    title="TruthLens API",
    description="AI-powered narrative & fact divergence analyzer",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "TruthLens is running"}

@app.post("/analyze")
def analyze(payload: dict):
    return analyze_articles(payload["articles"])

