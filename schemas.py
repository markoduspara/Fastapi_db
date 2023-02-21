from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price : float
    description: Optional[str] = None
    store_id: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class StoreBase(BaseModel):
    name: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
        
class RezultatBase(BaseModel):
    blob: str
    job_id: str
    target: str
    height: str
    seed_hash: str
    nonce: str
    hash: str
    

class RezultatCreate(RezultatBase):
    pass


class Rezultat(RezultatBase):
    id: int

    class Config:
        orm_mode = True
