from typing import Union

from fastapi import FastAPI, HTTPException
from api.events import router as event_router




app = FastAPI()
app.include_router(event_router, prefix="/api/events")
@app.get("/")
def  read_root():
    return {"Hello": "Worldwwww"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return  {"item_id": item_id, "q": q}

@app.get("/health")
def health_check():
    return {"status": "ok"}