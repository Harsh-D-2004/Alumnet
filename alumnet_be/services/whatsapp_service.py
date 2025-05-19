import requests
import os
from dotenv import load_dotenv
from services.vector_db_services import  search
import pywhatkit
from datetime import datetime, timedelta

env = load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"


def extract_number(user_query: str):
    context = search(user_query)
    print("context : " , context)

    prompt = f"""
You are a helpful assistant.  
Use the following context to answer the user's query.  

Context:  
{context}

User Query:  
{user_query}

Instruction:  
Return ONLY the phone number of the person mentioned in the query from the context.  
If no phone number is found, return 'Not available'.
Respond with the phone number as plain text, no extra words.
"""

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    res_json = response.json()

    return_data = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
    print("return_data : " ,  return_data)
    return return_data

def send_message_in_background(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"Message sent to {phone_number}")

def make_whatsapp_message(user_query: str):
    # phone_number = "+91"+ extract_number(user_query)
    phone_number = "+917038000319"
    
    if phone_number == "Not available":
        return "Sorry, I couldn't find a phone number for that person."
    else:

        now = datetime.now() + timedelta(minutes=1)
        hour = now.hour
        minute = now.minute

        print("hour : " , hour)
        print("minute : " , minute)

        message = "Hello! This is Harsh from the Training and Placement Office, PVG College. We are reaching out to reconnect with our esteemed alumni and would love to stay in touch regarding opportunities, networking, and future collaborations. Looking forward to connecting with you!"

        # background_tasks.add_task(send_message_in_background, phone_number, message, hour, minute)

        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message sent to {phone_number}")

        return f"I've scheduled a message to {phone_number} at {hour}:{minute}. Please check your WhatsApp."


