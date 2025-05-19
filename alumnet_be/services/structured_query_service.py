import requests
import os
from dotenv import load_dotenv

env = load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_cypher_query(user_query : str):
    
    schema = '''

    Nodes : 
        Alumni(name , passout_year , contact , email , linkedin )
        Company(name , industry , location , website , hr_contact , alumni_count )

    Relationships :
        (Alumni)-[:WORKED_AT]->(Company)
        WORKED_AT(department , from , to , job_title , placement_type(Off-Campus , On-Campus) )
        This relationship shows that alumni worked at company
'''

    prompt = '''

    You are a Cypher expert. Given the following Neo4j graph schema:

    {schema}

    Generate a cypher query to answer the following question:

    {question}

    Only return the cypher query and nothing else.

    '''

    data = {
        "contents": [
            {
                "parts": [{"text": prompt.format(schema=schema, question=user_query)}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    res_json = response.json()
    query = res_json["candidates"][0]["content"]["parts"][0]["text"]
    if query.lower().startswith("cypher"):
        query = query[6:].strip() 
    query = query.replace("```cypher", "").replace("```", "").strip()
    print(query)
    print(type(query))
    return query

def format_any_cypher_result(records):
    if not records:
        return "No records found."

    def format_record(record, indent=0):
        lines = []
        indent_str = "  " * indent
        for key, value in record.items():
            if isinstance(value, dict):
                lines.append(f"{indent_str}{key}:")
                lines.append(format_record(value, indent + 1))
            else:
                lines.append(f"{indent_str}{key}: {value}")
        return "\n".join(lines)

    formatted_records = [format_record(record) for record in records]
    return "\n\n".join(formatted_records)


def run_cypher_query(tx , query : str):

    cypher_query = generate_cypher_query(query)

    result = tx.run(cypher_query)
    records = result.data()
    records_return = format_any_cypher_result(records)
    better_response = response_bettement(query , records_return)
    return better_response

def response_bettement(query : str , cypher_result : str):
    print(cypher_result)
    if cypher_result is None or cypher_result == "":
        return "I am sorry, I could not find any relevant information."
    
    prompt = '''

You are a helpful assistant for an alumni database system. A user asked a query, and a database has returned the following result.

Your job is to convert this database result into a clean, readable, and user-friendly response.

- DO NOT explain the query.
- DO NOT mention the database.
- Focus only on turning the result into a natural plain text response for the user.
- If no useful data is found, say "Sorry, no relevant information was found."

User Query:
{query}

Database Result:
{result}

Respond with the final user-friendly plain text without formatting.

    '''

    data = {
        "contents": [
            {
                "parts": [{"text": prompt.format(query=query, result=cypher_result)}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    res_json = response.json()
    print(res_json)
    query = res_json["candidates"][0]["content"]["parts"][0]["text"]
    return query