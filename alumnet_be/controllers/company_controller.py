from services.company_service import create_company_node , update_company_node , get_comapny_node , delete_company_node
from database import get_driver
from fastapi import APIRouter
from models.company import Company 

driver = get_driver()
router = APIRouter()


@router.post('/')
async def create_company(company : Company):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        company_id = create_company_node(session , company)
        if company_id is None:
            return {"message" : "Company creation failed"}
        return {"id" : company_id}
    
@router.get('/{company_id}')
async def get_company(company_id):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        company = session.execute_read(get_comapny_node , company_id)
        if company is None:
            return {"message" : "Company not found"}
        return {company}
    
@router.put('/{company_id}')
async def update_company(company_id : str , company : Company):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        company_id = session.execute_write(update_company_node , company_id , company)
        return {"id" : company_id}
    
@router.delete('/{company_id}')
async def delete_company(company_id : str):
    if driver is None:
        return {"message" : "Database not connected"}
    with driver.session() as session:
        company_id = session.execute_write(delete_company_node , company_id)
        return {"id" : company_id}