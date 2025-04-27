from fastapi import HTTPException, status
from .models import EventIn, EventDb, PlayerDb
from sqlmodel import Session, select
from datetime import datetime

EVENT_TYPES = {"level_started", "level_solved"}

def get_events_by_player_id(session: Session, player_id: int, event_type: str = None):
    query = select(EventDb).where(EventDb.player_id == player_id)
    if event_type:
        query = query.where(EventDb.type == event_type)
    events = session.exec(query).all()
    if not events:
        raise HTTPException(detail = f"No events found for player {player_id}.", status_code = status.HTTP_404_NOT_FOUND)
    return events

def create_event(session: Session, player_id: int, event_in: EventIn):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(detail = f"Player {player_id} not found.", status_code = status.HTTP_404_NOT_FOUND)
    if event_in.type not in EVENT_TYPES:
        raise HTTPException(detail = "Invalid event type.", status_code = status.HTTP_400_BAD_REQUEST)

    e = EventDb(**event_in.dict(), timestamp = datetime.now(), player_id = player_id)
    session.add(e)
    session.commit()
    session.refresh(e)
    return e

def get_all_events(session: Session, event_type: str = None):
    query = select(EventDb)
    if event_type:
        query = query.where(EventDb.type == event_type)
    events = session.exec(query).all()
    if event_type not in EVENT_TYPES:
        raise HTTPException(detail = "Invalid event type.", status_code = status.HTTP_400_BAD_REQUEST)
    return events