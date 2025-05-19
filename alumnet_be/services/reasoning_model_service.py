import requests
import os
from dotenv import load_dotenv

env = load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_text(context : str , user_query : str):

    data = {
        "contents": [
            {
                "parts": [{"text": f"You are a helpful assistant. Use the following context to answer the question:\n\nContext:\n{context}\n\nQuestion:\n{user_query}Return answer in plain text."}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    res_json = response.json()
    return_data = res_json["candidates"][0]["content"]["parts"][0]["text"]
    return return_data