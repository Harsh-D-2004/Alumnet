from pydantic import BaseModel

class Alumni(BaseModel):
    name: str
    passout_year: int
    contact: str
    email: str
    linkedin: str