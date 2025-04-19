from typing import Optional
from pydantic import BaseModel


class create_house(BaseModel):
    name : str
    address : str
    city : str 
    bedrooms : int
    bathrooms : int 

class update_house(BaseModel):
    name : Optional[str] = None 
    address : Optional[str] = None 
    city  : Optional[str] = None 
    bedrooms : Optional[str] = None 
    bathrooms : Optional[str] = None 
    
class estateFetch(BaseModel):
    id : Optional[int] = None 
    estate : str 

class estateSearch(BaseModel):
    id : int 
