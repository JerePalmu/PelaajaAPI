from fastapi import status, HTTPException
from .models import PlayerIn, PlayerDb
from sqlmodel import Session, select

players = [
    {"id": 0, "name": "Pelaaja 1"},
    {"id": 1, "name": "Pelaaja 2"},
    {"id": 2, "name": "Pelaaja 3"},
]

def create_player(session: Session, player_in: PlayerIn):
    s = PlayerDb.model_validate(player_in)
    session.add(s)
    session.commit()
    session.refresh(s)
    return s

def get_players(session: Session, name: str = ""):
    if name != "":
        return session.exec(select(PlayerDb).where(PlayerDb.name == name)).all()
    return session.exec(select(PlayerDb)).all()

def get_player_by_id(session: Session, player_id: int):
    s = session.get(PlayerDb, player_id)
    if not s:
        raise HTTPException(detail = f"Player {player_id} not found.", status_code = status.HTTP_404_NOT_FOUND)