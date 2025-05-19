from fastapi import APIRouter
from services.mail_service import make_mail_message
from models.query import Query

router = APIRouter()

@router.post("/mail")
async def send_mail(payload: Query):
    user_query = payload.query
    response = make_mail_message(user_query)
    return {
        "result": response
    }