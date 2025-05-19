from services.reasoning_model_service import generate_text
from models.query import Query
from fastapi import APIRouter
from database import get_driver
from services.vector_db_services import search

router = APIRouter()

driver = get_driver()

@router.post("/ask")
async def ask_llm(payload: Query):
    user_query = payload.query

    context_data = search(user_query)

    response = generate_text(context_data , user_query)

    return {
        "result": response
    }



