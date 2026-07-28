from fastapi import FastAPI

app = FastAPI(
    title="CloudOps ServiceDesk API",
    description="Enterprise-style IT Service Management Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CloudOps ServiceDesk API",
        "status": "Running",
        "version": "1.0.0"
    }