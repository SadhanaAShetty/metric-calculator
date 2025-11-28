from fastapi import FastApi



app = FastApi

@app.post("/user_id")
def upload_data():
    return {"message": "Hello, FastAPI!"}

@app.get("/user_id")
def get_metrics():
    return {"message": "Hello, FastAPI!"}

@app.get("/user_id")
def get_api_reports():
    return {"message": "Hello, FastAPI!"}

@app.get("/user_id")
def get_trends():
    return {"message": "Hello, FastAPI!"}