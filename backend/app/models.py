from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Date(BaseModel):
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()


class Active(BaseModel):
    active: bool = True


class SuperEnum(Enum):
    @classmethod
    def values(cls):
        return [e.value for e in cls]


class ItemSearch(BaseModel):
    text: str | None = None


class ItemCreate(BaseModel):
    title: str
    meaning: str


class Item(Date, Active, ItemCreate):
    pass
