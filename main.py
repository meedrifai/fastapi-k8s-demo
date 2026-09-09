from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI + Kubernetes!",
        "pod": socket.gethostname()
    }
