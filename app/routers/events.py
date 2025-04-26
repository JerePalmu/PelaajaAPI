from fastapi import APIRouter, status, Depends
from ..db.models import EventIn, EventDb
from ..db import events_crud
from ..db.database import get_session
from sqlmodel import Session
from typing import Optional

router = APIRouter()

@router.get("/players/{id}/events", response_model = list[EventDb])
def get_events_for_player(player_id: int, type: Optional[str] = None, session: Session = Depends(get_session)):
    return events_crud.get_events_by_player_id(session, player_id, type)

@router.post("/players/{id}/events", status_code = status.HTTP_201_CREATED)
def create_event(player_id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return events_crud.create_event(session, player_id, event_in)

@router.get("/events", response_model = list[EventDb])
def get_all_events(type: Optional[str] = None, session: Session = Depends(get_session)):
    return events_crud.get_all_events(session, type)