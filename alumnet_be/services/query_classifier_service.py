from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableBranch
from controllers.structured_query_controller import structured_query
from controllers.reasoning_model_controller import ask_llm
from controllers.whatsapp_controller import whatsapp
from controllers.mail_controller import send_mail
from models.vector_db import Search_Query
import requests
import os
from dotenv import load_dotenv


env = load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"


def classify_query_llm(query: Search_Query) -> str:

    prompt = """ 

    We are querying an alumni and company database which uses:
    - A **vector database with RAG + LLM** for general and fact-based queries.
    - A **graph database (Neo4j)** for structured aggregation queries.

    **Query classification rules:**

    1. **structured_query**  
       For aggregation-type queries that request:
       - A count, number, or list of people, employees, alumni, or companies.
       - Or queries that ask for totals or enumerations.

    2. **whatsapp_query**  
       For queries about sending WhatsApp messages, e.g.:
       - "Can you message Cathy?"
       - "Send a WhatsApp to John"
       - "Message HR about the offer."

    3. **mail_query**  
       For queries about sending emails, e.g.:
       - "Can you mail this to HR?"
       - "Send an email to Cathy."
       - "Mail the alumni list."

    4. **general_query**  
       All other queries related to alumni, employees, or companies that don't fall into the above categories.

    5. **default_query**  
       For queries unrelated to alumni, employees, companies, WhatsApp, or email.

    ---

    **Classify the following query into one of these keywords:**
    - `structured_query`
    - `whatsapp_query`
    - `mail_query`
    - `general_query`
    - `default_query`

    **Query:**  
    "{input}"

    **Return ONLY the keyword as plain string — nothing else.**

    """
    data = {
        "contents": [
            {
                "parts": [{"text": prompt.format(input=query.query)}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    res_json = response.json()
    query_type = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()

    ret = {"type" : query_type , "query" : query}

    print(ret)
    return ret
    
query_classifier = RunnableLambda(classify_query_llm)

async def async_structured_query_wrapper(data):
    return await structured_query(data["query"])

async def async_general_query_wrapper(data):
    return await ask_llm(data["query"])

async def async_whatsapp_query_wrapper(data):
    return await whatsapp(data["query"])

async def async_mail_query_wrapper(data):
    return await send_mail(data["query"])

async def async_default_query_wrapper(data):
    return {"result": "It seems your query is outside the scope of our alumni and company database. Try asking about people, companies, or connections."}

cypher_query_chain = RunnableLambda(async_structured_query_wrapper)
general_query_chain = RunnableLambda(async_general_query_wrapper)
whatsapp_query_chain = RunnableLambda(async_whatsapp_query_wrapper)
mail_query_chain = RunnableLambda(async_mail_query_wrapper)
default_chain = RunnableLambda(lambda x: x["type"] == "default_query" , async_default_query_wrapper)

router_chain = (
    query_classifier |
    RunnableBranch(
        (lambda x: x["type"] == "structured_query", cypher_query_chain),
        (lambda x: x["type"] == "general_query", general_query_chain),
        (lambda x: x["type"] == "whatsapp_query", whatsapp_query_chain),
        (lambda x: x["type"] == "mail_query", mail_query_chain),
        default_chain,
    )
)

async def getResponse(query : Search_Query):
    output = await router_chain.ainvoke(query)
    print(output)
    return output

