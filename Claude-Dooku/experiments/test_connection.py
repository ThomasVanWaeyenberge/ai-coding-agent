import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("endpoint")
model_name = os.getenv("model_name")
deployment_name = os.getenv("deployment_name")
api_key = os.getenv("api_key")


client = OpenAI(
    base_url=f"{endpoint}",
    api_key=api_key
    )

completion = client.chat.completions.create(
model=deployment_name,
messages=[
    {
    "role": "user",
    "content": "What is the capital of France?",
    }
    ],
)

print(completion.choices[0].message)
