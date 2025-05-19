from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from services.context_services import preprocess_context
import os
from dotenv import load_dotenv

env = load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pc.Index("alumni-index")
embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def upsert_all(context):
    for record in context:
        upsert(record)

def upsert(record):
    formatted_text = preprocess_context(record)
    embedding = embed_model.embed_query(formatted_text)
    index.upsert([
        (record["alumni"]["name"], embedding, {"text": formatted_text})
    ])
    return formatted_text

def search(search_query : str):
    query_vector = embed_model.embed_query(search_query) 
    results = index.query(vector=query_vector, top_k=2, include_metadata=True)
    return_data = [match["metadata"]["text"] for match in results["matches"]]
    return_string = "\n".join(return_data)
    return return_string

def search_k_is_1(search_query : str):
    query_vector = embed_model.embed_query(search_query) 
    results = index.query(vector=query_vector, top_k=1, include_metadata=True)
    return_data = [match["metadata"]["text"] for match in results["matches"]]
    return_string = "\n".join(return_data)
    return return_string