from fastapi import FastApi, HTTPException
import time




app = FastApi

@app.post("/user_id")
def upload_data():

    required_keys = ["user_id","time_stamp","glucose_mmol" ]
    try:

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