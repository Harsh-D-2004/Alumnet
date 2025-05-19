from pydantic import BaseModel

class Search_Query(BaseModel):
    query : str