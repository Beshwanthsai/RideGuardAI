from fastapi import FastAPI

app = FastAPI(title="RideGaurdAI")

@app.get("/")
def Home():
    return {
        "message":"Welcome to RideGaurdAI"
    }
    