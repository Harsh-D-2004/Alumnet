from models.alumni import Alumni
from services.alumni_service import create_alumni_node , get_alumni_node , update_alumni_node , delete_alumni_node
from database import get_driver
from fastapi import APIRouter

driver = get_driver()
router = APIRouter()

@router.post("/")
async def create_alumni(alumni: Alumni):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        alumni_id = create_alumni_node(session , alumni)
        return {"id" : alumni_id}

@router.get("/{alumni_id}")
async def get_alumni(alumni_id):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        alumni = session.execute_read(get_alumni_node , alumni_id)
        if(alumni is None):
            return {"message" : "Alumni not found"}
        return alumni

@router.put("/{alumni_id}")
async def update_alumni(alumni_id , alumni: Alumni):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        alumni_id = session.execute_write(update_alumni_node , alumni_id , alumni)
        return {"id" : alumni_id}

@router.delete("/{alumni_id}")
async def delete_alumni(alumni_id):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        alumni_id = session.execute_write(delete_alumni_node , alumni_id)
        return {"id" : alumni_id}