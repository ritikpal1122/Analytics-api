from pydantic import BaseModel
from typing import List


class EventSchema(BaseModel):
    id: int 
    
    
    
# id: int

class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int