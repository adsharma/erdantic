from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from erdantic import create_erd


class Adventurer(BaseModel):
    name: str
    profession: str
    level: int
    affinity: str


class QuestGiver(BaseModel):
    name: str
    faction: Optional[str]
    location: str


class Quest(BaseModel):
    name: str
    giver: QuestGiver
    reward_gold: int


class Party(BaseModel):
    name: str
    formed_datetime: datetime
    members: List[Adventurer]
    active_quest: Optional[Quest]


def test_model_crawling():
    diagram = create_erd(Party)
    assert {m.pydantic_model for m in diagram.models} == {Party, Adventurer, Quest, QuestGiver}