from fastapi import APIRouter, Depends, status, Query
from ..db.models import EventIn, EventDb
from ..db import events_crud
from ..db.database import get_session
from sqlmodel import Session
from typing import List, Optional

router = APIRouter(prefix="/players")

@router.post("/{player_id}/events", response_model=EventDb, status_code=status.HTTP_201_CREATED)
def create_event(player_id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return events_crud.create_event(session, player_id, event_in)

@router.get("/{player_id}/events", response_model=List[EventDb])
def get_player_events(player_id: int, type: str = None, session: Session = Depends(get_session)):
    return events_crud.get_events_for_player(session, player_id, type)