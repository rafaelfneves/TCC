from __init__ import *
from models import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    year = Column(Integer)
    plate = Column(String)
    fk_collector = Column(String(11), ForeignKey('collectors.cpf'))
    collector = relationship('Collector')
    capacity_kg = Column(Float)
