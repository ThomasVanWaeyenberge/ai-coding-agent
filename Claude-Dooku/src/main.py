import os
import random
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

dooku_quotes = [
    "I have been trained in your Jedi arts by Count Dooku.",
    "Twice the pride, double the fall.",
    "I sense great fear in you, Skywalker. You have hate... you have anger",
    "The dark side of the Force is a pathway to many abilities some consider to be unnatural"
]

system_prompt = """You are Count Dooku, a character from Star Wars and you write code """

def get_random_dooku_quote() -> str: 
    return random.choice(dooku_quotes)

def add_to_history_and_get_dooku_response(history: list[dict[str, str]], user_input: str) -> str:
    history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=deployment_name,
        messages=history,
    )

    assistant_message = response.choices[0].message
    history.append({
        "role": assistant_message.role,
        "content": assistant_message.content
    })

    return assistant_message.content

history: list[dict[str, str]] = [
        {
            "role": "system",
            "content": system_prompt
        }
]

def main():
    print("Claude Dooku is running. Type /help for commands!")
    while True:
        try:
            text = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\n")
            print(get_random_dooku_quote())
            break

        text = text.strip()
        if not text:
            continue

        if text == "/exit":
            print(get_random_dooku_quote())
            break
        if text == "/help":
            print("Commands: /help, /exit")
            continue

        response = add_to_history_and_get_dooku_response(history, text)
        print(response)

if __name__ == "__main__": 
    main() 