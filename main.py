from fastapi import FastAPI, Body
from dotenv import load_dotenv
import os
import openai

# Load env variables
load_dotenv(".env")
openai.api_key = os.environ["OPENAI_KEY"]

# Create FastAPI
app = FastAPI()
app.title = "Dapta ChatGPT API"


@app.get("/")
def index():
    return "Dapta ChatGPT API"


@app.post("/ask")
def ask_chatgpt(question: str = Body()):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a spanish speaking friendly assistant."},
            {"role": "user", "content": question}
        ]
    )
    print(response)
    parsed_response = response.choices[0].message.content
    return parsed_response
