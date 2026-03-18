from fastapi import FastAPI

app = FastAPI(title="Eagle-Eyed Scholars")

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}