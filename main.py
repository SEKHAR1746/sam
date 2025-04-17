from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return {"1": "Sugar", "2": "Salt", "3": "pepper"}