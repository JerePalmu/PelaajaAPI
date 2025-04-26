from fastapi import APIRouter, status, Depends
from ..db.models import PlayerIn, PlayerDb
from ..db import players_crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter()

@router.post("/players/", status_code = status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return players_crud.create_player(session, player_in)

@router.get("/players/", response_model = list[PlayerDb])
def get_players(session: Session = Depends(get_session)):
    return players_crud.get_players(session)

@router.get("/players/{id}", response_model = PlayerDb)
def get_player_by_id(player_id: int, session: Session = Depends(get_session)):
    return players_crud.get_player_by_id(session, player_id)