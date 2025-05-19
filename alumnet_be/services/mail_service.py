import requests
import os
from dotenv import load_dotenv
from services.vector_db_services import  search
import pywhatkit
from datetime import datetime

env = load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def extract_mail(user_query: str):
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
Return ONLY the mail of the person mentioned in the query from the context.  
If no mail is found, return 'Not available'.
Respond with the mail as plain text, no extra words.
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

def make_mail_message(user_query: str):
    # mail = extract_mail(user_query)
    mail = "hdoshi319@gmail.com"
    
    if mail == "Not available":
        return "Sorry, I couldn't find a phone number for that person."
    else:

        now = datetime.now()
        hour = now.hour
        minute = now.minute

        print("hour : " , hour)
        print("minute : " , minute)

        header = "Placement Collaboration Opportunity with PVG College"
        message = '''I hope this message finds you well.

I am Harsh, representing the Training and Placement Office at PVG College, Pune. We are keen on building and strengthening our association with esteemed organizations like yours for potential placement drives and hiring opportunities for our graduating students.

Our students are well-trained in both technical and interpersonal skills, and we would be delighted to connect with you regarding any current or upcoming vacancies, internship programs, or campus recruitment initiatives at [Company Name].

We would be grateful if you could share available opportunities or let us know a convenient time for a brief discussion.

Looking forward to hearing from you and hoping for a fruitful collaboration.

Warm regards,
Harsh
Training and Placement Officer
PVG College, Pune'''

        pywhatkit.send_mail("harshburner2004@gmail.com", "wiuhtaymfsjhcvtx" , header, message, mail)

        return f"Mail sent to {mail} at {hour}:{minute}. Please check your mail."