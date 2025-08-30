from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter() # this API router will be used to define event-related endpoints


# /api/events/
@router.get("/") # we use @ for decorators
def read_events():
    # a bunch of logic to read events from a database or other source would go here
    return {"events": [1,2,3]}  # Placeholder implementation

# /api/events/{event_id}
@router.get("/{event_id}")
def get_events(event_id: int) -> EventSchema: 
    # logic to read a specific event by its ID would go here
    return {"id": event_id, "name": f"Event {event_id}"}  # Placeholder implementation

