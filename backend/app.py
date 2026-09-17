from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello IEEE DevOps!"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/testing")
def testing():
    return {"message": "This is a testing endpoint."}