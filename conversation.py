import openai
from dotenv import load_dotenv
import os

load_dotenv(".env")

openai.api_key = os.environ["OPENAI_KEY"]

messages = [
    {"role": "system", "content": "You are a spanish speaking friendly assistant."}]

while True:
    question = input("Háblame... \n")

    if question == "exit":
        break

    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(response.choices[0].message.content)
