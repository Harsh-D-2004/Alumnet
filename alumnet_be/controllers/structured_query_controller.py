from services.structured_query_service import run_cypher_query
from fastapi import APIRouter
from database import get_driver
from models.vector_db import Search_Query

router = APIRouter()

driver = get_driver()

@router.post("/query")
async def structured_query(search_query : Search_Query):

    with driver.session() as session:
        result = run_cypher_query(session , search_query.query)
        print("result controller: " , result)
        return {"result": result}