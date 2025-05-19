from services.query_classifier_service import getResponse
from models.vector_db import Search_Query
from fastapi import APIRouter

router = APIRouter()

@router.post("/query")
async def query_classifier(search_query : Search_Query):
    return await getResponse(search_query)