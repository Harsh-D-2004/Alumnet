from services.vector_db_services import search
from services.vector_db_services import search_k_is_1
from fastapi import APIRouter
from models.vector_db import Search_Query

router = APIRouter()

@router.post("/search")
async def search_alumni(search_query : Search_Query):
    results = search(search_query.query)
    return {"results" : results}

@router.post("/search_k_is_1")
async def search_alumni_one(search_query : Search_Query):
    results = search_k_is_1(search_query.query)
    return {"results" : results}