from fastapi import status, HTTPException
from .models import PlayerIn, PlayerDb
from sqlmodel import Session, select

players = [
    {"id": 0, "name": "Pelaaja 1"},
    {"id": 1, "name": "Pelaaja 2"},
    {"id": 2, "name": "Pelaaja 3"},
]

def create_player(session: Session, player_in: PlayerIn, player_id: int):
    s = PlayerDb.model_validate(player_in, player_id)
    session.add(s)
    session.commit()
    session.refresh(s)
    if not s:
        raise HTTPException(detail = f"Player {player_id} couldn't be created.", status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    return s

def get_players(session: Session):
    return session.exec(select(PlayerDb)).all()

def get_player_by_id(session: Session, player_id: int):
    s = session.get(PlayerDb, player_id)
    if not s:
        raise HTTPException(detail = f"Player {player_id} not found.", status_code = status.HTTP_404_NOT_FOUND)