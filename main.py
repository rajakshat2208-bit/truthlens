from fastapi import FastAPI

app = FastAPI(title="TruthLens API")

@app.get("/")
def root():
    return {"message": "TruthLens API is running"}

@app.post("/analyze")
def analyze(data: dict):
    return {
        "status": "success",
        "input": data,
        "note": "Pipeline temporarily disabled for deployment"
    }
