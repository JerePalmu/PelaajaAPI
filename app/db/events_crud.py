from fastapi import HTTPException, status
from .models import EventIn, EventDb, PlayerDb
from sqlmodel import Session, select
from datetime import datetime

EVENT_TYPES = {"level_started", "level_solved"}

def create_event(session: Session, player_id: int, event_in: EventIn):
    if event_in.type not in EVENT_TYPES:
        raise HTTPException(detail = "Invalid event type.", status_code = status.HTTP_400_BAD_REQUEST)

    e = EventDb(player_id=player_id, timestamp=datetime.now())
    session.add(e)
    session.commit()
    session.refresh(e)
    return e

def get_events_for_player(session: Session, player_id: int, type: str = None):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(detail = "Player not found.", status_code = status.HTTP_404_NOT_FOUND)

    query = select(EventDb).where(EventDb.player_id == player_id)
    if type:
        if type not in EVENT_TYPES:
            raise HTTPException(detail = "Invalid event type.", status_code = status.HTTP_400_BAD_REQUEST)
        query = query.where(EventDb.type == type)
    return session.exec(query).all()