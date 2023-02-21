from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True,index=True)
    price = Column(Float(precision=2), nullable=False)
    description = Column(String(200))
    store_id = Column(Integer,ForeignKey('stores.id'),nullable=False)
    def __repr__(self):
        return 'ItemModel(name=%s, price=%s,store_id=%s)' % (self.name, self.price,self.store_id)
    
class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True)
    items = relationship("Item",primaryjoin="Store.id == Item.store_id",cascade="all, delete-orphan")

    def __repr__(self):
        return 'Store(name=%s)' % self.name
    
class Rezultat(Base):
    __tablename__ = "rezultati"
    id = Column(Integer, primary_key=True,index=True)
    blob = Column(String(300), nullable=False, unique=False,index=True)
    height = Column(String(300), nullable=False, unique=False,index=True)
    job_id = Column(String(10), nullable=False, unique=False)
    target = Column(String(300), nullable=False, unique=False)
    seed_hash = Column(String(300), nullable=False, unique=False)
    hash = Column(String(300), nullable=True, unique=False)
    nonce = Column(String(300), nullable=True, unique=False)
    

    def __repr__(self):
        return 'Rezultat(blob=%s, height=%s, job_id=%s, target=%s, seed_hash=%s, hash=%s, nonce=%s)' % (self.blob,self.height,self.job_id,self.target,self.seed_hash,self.hash,self.nonce)
