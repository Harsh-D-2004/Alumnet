from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_driver
from controllers.alumni_controller import router as alumni_router
from controllers.company_controller import router as company_router
from controllers.context_controller import router as context_router
from controllers.vector_db_controller import router as vector_db_router
from controllers.reasoning_model_controller import router as reasoning_model_router
from controllers.structured_query_controller import router as structured_query_router
from controllers.query_classifier_controller import router as ask_router
from controllers.whatsapp_controller import router as whatsapp_router
from controllers.mail_controller import router as mail_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

driver = get_driver()
print("Driver : " , driver)

@app.get("/")
async def root():
    if driver is None:
        return {"message" : "Database not connected"}
    return {"message" : "Server running"}

app.include_router(alumni_router, prefix="/alumni", tags=["Alumni"])
app.include_router(company_router, prefix="/company", tags=["Company"])
app.include_router(context_router, prefix="/context", tags=["Context"])
app.include_router(vector_db_router, prefix="/vector_db", tags=["Vector DB"])
app.include_router(reasoning_model_router, prefix="/reasoning_model", tags=["Reasoning Model"])
app.include_router(structured_query_router, prefix="/structured_query", tags=["Structured Query"])
app.include_router(ask_router, prefix="/ask", tags=["ask result"])
app.include_router(whatsapp_router, prefix="/ask", tags=["Whatsapp"])
app.include_router(mail_router, prefix="/ask", tags=["Mail"])