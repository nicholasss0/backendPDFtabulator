from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from google import genai

import tabula
import pandas as pd
import tempfile

import os
import requests
import dotenv

dotenv.load_dotenv()
app = FastAPI()


api_key = os.getenv("GEMINI_KEY")
modelAi = "gemini-2.0-flash"

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/gemini/{query}")
async def reply(query):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=modelAi, contents=query
    )
    
    answer = response.text
    return { "query" : answer }


@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    with open(file, 'r'):
        file_content = file.file.read()
    
    


