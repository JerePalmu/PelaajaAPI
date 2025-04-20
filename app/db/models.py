from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class PlayerBase(SQLModel):
    name: str

class PlayerIn(PlayerBase):
    pass

class PlayerDb(PlayerBase, table = True):
    id: int = Field(default = None, primary_key = True)