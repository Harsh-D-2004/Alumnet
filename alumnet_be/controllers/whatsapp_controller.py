from fastapi import APIRouter
from services.whatsapp_service import make_whatsapp_message
from models.query import Query


router = APIRouter()

@router.post("/whatsapp")
async def whatsapp(user_query : Query):
    query = user_query.query
    ret =  make_whatsapp_message(query)
    return {"result": ret}