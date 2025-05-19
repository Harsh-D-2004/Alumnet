
from pydantic import BaseModel


class Company(BaseModel):
    name : str
    industry : str
    location : str
    website : str
    hr_contact : str
    alumni_count : str