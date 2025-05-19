from services.context_services import get_graph_context
from fastapi import APIRouter
from database import get_driver
from services.vector_db_services import upsert

router = APIRouter()

driver = get_driver()

@router.get("/graph_data")
async def get_graph_data():
    context = driver.session().execute_read(get_graph_context)
    for record in context:
        print(type(record))
        upsert(record)
    return context